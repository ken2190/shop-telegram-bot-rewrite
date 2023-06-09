from typing import Any
import database
from . import items


class Category:
    def __init__(self, id: int) -> None:
        self.id = id
    
    async def __query(self, field: str) -> Any:
        return (await database.fetch(f"SELECT {field} FROM categories WHERE id = ?", self.id))[0][0]

    async def __update(self, field: str, value: Any) -> None:
        await database.fetch(f"UPDATE categories SET {field} = ? WHERE id = ?", value, self.id)

    @property
    def database_table(self) -> str:
        return """CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            parent_id INTEGER,
            is_hidden INTEGER,
            FOREIGN KEY (parent_id) REFERENCES categories (id)
        )"""

    @property
    async def name(self) -> str:
        return await self.__query("name")
    async def set_name(self, value: str) -> None:
        await self.__update("name", value)

    @property
    async def parent_id(self) -> int:
        return await self.__query("parent_id")
    async def set_parent_id(self, value: int) -> None:
        await self.__update("parent_id", value)
    
    @property
    async def parent(self) -> Any | None:
        parent_id = await self.parent_id
        return Category(parent_id) if parent_id != 0 else None
    async def set_parent(self, value: "Category") -> None:
        await self.__update("parent_id", value.id)

    @property
    async def is_hidden(self) -> bool:
        return bool(await self.__query("is_hidden"))
    async def set_is_hidden(self, value: bool) -> None:
        await self.__update("is_hidden", int(value))

    @property
    async def children(self) -> list["Category"]:
        return [Category(*id) for id in await database.fetch("SELECT id FROM categories WHERE parent_id = ?", self.id)]
    
    @property
    async def items(self) -> list["Item"]:
        return [items.Item(*id) for id in await database.fetch("SELECT id FROM items WHERE category_id = ? AND is_hidden = 0", self.id)]

    @property
    async def all_items(self) -> list["Item"]:
        return [items.Item(*id) for id in await database.fetch("SELECT id FROM items WHERE category_id = ?", self.id)]
    
    async def delete(self) -> None:
        await database.fetch("DELETE FROM categories WHERE id = ?", self.id)

async def get_categories() -> list[Category]:
    return [Category(*id) for id in await database.fetch("SELECT id FROM categories")]

async def get_main_categories() -> list[Category]:
    return [Category(*id) for id in await database.fetch("SELECT id FROM categories WHERE parent_id=0 AND is_hidden=0")]

async def does_category_exist(id: int) -> bool:
    return (await database.fetch("SELECT id FROM categories WHERE id = ?", id))[0][0] == id

async def create(name: str, parent_id: int = 0) -> Category:
    await database.fetch("INSERT INTO categories (name, parent_id, is_hidden) VALUES (?, ?, 0)", name, parent_id)
    return Category((await database.fetch("SELECT id FROM categories ORDER BY id DESC LIMIT 1"))[0][0])

