import asyncio
from os import listdir
import importlib
from json import loads
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from constants import *
from config import config
from markups import markups
import models.users as users
import models.items as items
import utils
import database
import dotenv

# First startup
if not os.path.exists("database.db"):
    tasks = [
        database.execute(object.database_table)
        for object in [users, items]
    ]
    asyncio.run(asyncio.gather(*tasks))
if not os.path.exists("config.json"):
    config.init()


dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = os.getenv("TOKEN")
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message) -> None:
    user = users.User(message.chat.id)

    markup = markups.main
    if user.is_admin:
        markup.add(types.KeyboardButton(language.admin_panel))
    if user.is_admin or user.is_manager:
        markup.add(types.KeyboardButton(language.orders))

    if "sticker.tgs" in listdir("."):
        with open("sticker.tgs", "rb") as sticker:
            await bot.send_sticker(user.id, sticker)

    await bot.send_message(
        chat_id=user.id,
        text=config["info"]["greeting"],
        reply_markup=markup,
    )

@dp.message_handler()
async def handle_text(message: types.Message) -> None:
    user = users.User(message.chat.id)
    text = language.unknown_command
    markup = types.InlineKeyboardMarkup()

    match message.text:
        case language.catalogue:
            markup = markups.catalogue(categories.cat_list())
        case language.cart:
            markup = markups.cart
        case language.profile:
            markup = markups.profile
        case language.faq:
            markup = markups.faq
        case language.admin_panel:
            if not user.is_admin:
                return await utils.sendNoPermission(bot, user.id)
            markup = markups.adminPanel
        case language.orders:
            if not user.is_manager and not user.is_admin:
                return await utils.sendNoPermission(bot, user.id)
            markup = markups.orders
    
    text = text if markup == types.InlineKeyboardMarkup() else message.text
    await bot.send_message(
        chat_id=user.id,
        text=text,
        reply_markup=markup,
    )
    

# A call sends json data at the start i.e. '{"role":admin,"item_id":10}deleteItem'
@dp.callback_query_handler()
async def process_callback(callback_query: types.CallbackQuery) -> None:
    call = callback_query.data
    user = users.User(callback_query.message.chat.id)
    data = loads(call[:call.index("}")+1])
    call = call[call.index("}")+1:]
    execute_args = (bot, user, callback_query.message.message_id, data)

    if config["settings"]["debug"]:
        print(f"{call} | [{user.id}] | {data}")
    if call == "None": return

    if data["role"] == "admin" and not user.is_admin:
        return await utils.sendNoPermission(bot, user.id)
    elif data["role"] == "manager" and (not user.is_admin or not user.is_manager):
        return await utils.sendNoPermission(bot, user.id)

    return await importlib.import_module(f"callbacks.{data['role']}.{call}").execute(*execute_args)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

