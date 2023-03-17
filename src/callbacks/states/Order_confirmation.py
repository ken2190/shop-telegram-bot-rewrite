from aiogram import types
from aiogram.dispatcher import FSMContext
import models
import constants
from markups import markups

async def execute(callback_query: types.CallbackQuery, user: models.users.User, data: dict, state: FSMContext, message: types.Message=None) -> None:
    call = callback_query.data[callback_query.data.index("}")+1:]

    await state.update_data()
    state_data = await state.get_data()

    await callback_query.message.edit_text(
        text=constants.language.None,
        reply_markup=markups.create([

        ])
    )


