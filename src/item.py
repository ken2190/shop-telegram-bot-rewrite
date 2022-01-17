import sqlite3
from settings import Settings

conn = sqlite3.connect("data.db")
c = conn.cursor()
settings = Settings()

def does_item_exist(item_id):
    c.execute(f"SELECT * FROM items WHERE id=?", [item_id])
    return len(list(c)) == 1


class Item:
    def __init__(self, item_id):
        self.__item_id = item_id
        
    def __eq__(self, __o: object):
        return self.get_id() == __o.get_id()
    
    def __repr__(self):
        return f"[{self.get_id()}] {self.get_name()}"

    def get_id(self):
        return self.__item_id
    
    def __clist(self):
        c.execute(f"SELECT * FROM items WHERE id=?", [self.get_id()])
        return list(c)[0]

    def get_name(self):
        return self.__clist()[1]

    def set_name(self, value):
        c.execute(f"UPDATE items SET name=? WHERE id=?", [value, self.get_id()])
        conn.commit()

    def get_price(self):
        return self.__clist()[2]

    def set_price(self, value):
        c.execute(f"UPDATE items SET price=? WHERE id=?", [value, self.get_id()])
        conn.commit()

    def get_cat_id(self):
        return self.__clist()[3]

    def set_cat_id(self, value):
        c.execute(f"UPDATE items SET cat_id=? WHERE id=?", [value, self.get_id()])
        conn.commit()

    def get_desc(self):
        return self.__clist()[4]

    def set_desc(self, value):
        c.execute(f"UPDATE items SET desc=? WHERE id=?", [value, self.get_id()])
        conn.commit()

    def is_active(self):
        return self.__clist()[5] == 1

    def set_active(self, value):
        c.execute(f"UPDATE items SET active=? WHERE id=?", [value, self.get_id()])
        conn.commit()

    def get_amount(self):
        return int(self.__clist()[6])
    
    def set_amount(self, value):
        c.execute(f"UPDATE items SET amount=? WHERE id=?", [value, self.get_id()])
        conn.commit()
        
    def get_image_id(self):
        return self.__clist()[7]
    
    def get_image(self):
        return open("images/" + self.get_image_id(), "rb")
    
    def set_image_id(self, value):
        c.execute(f"UPDATE items SET image_id=? WHERE id=?", [value, self.get_id()])

    def delete(self):
        c.execute(f"DELETE FROM items WHERE id=?", [self.get_id()])
        conn.commit()


def get_item_list():
    c.execute("SELECT * FROM items")
    return map(Item, [item[0] for item in list(c)])


def create_item(name, price, cat_id, desc, image_id="None"):
    c.execute(f"INSERT INTO items(name, price, cat_id, desc, active, amount, image_id) VALUES(?, ?, ?, ?, 1, 0, ?)", [name, price, cat_id, desc, image_id])
    conn.commit()

