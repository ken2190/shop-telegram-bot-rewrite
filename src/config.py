import os
import json
from typing import Any

filename = "config.json"
class Config:
    def __repr__(self):
        return self.__data 

    def __iter__(self):
        return self.__data

    def __getitem__(self, item):
        return self.__data[item]

    def __str__(self) -> str:
        return self.__raw 

    @property
    def __raw(self) -> str:
        with open(filename, "r") as f:
            return f.read()

    @property
    def __data(self):
       return json.loads(self.__raw) 

    def set(self, param: str | tuple[str, str], value: Any) -> None:
        modified_data = self.__data

        if isinstance(param, tuple):
            modified_data[param[0]][param[1]] = value
        else:
            modified_data[param] = value

        backup_filename = f"{filename}.bak"
        if os.path.exists(backup_filename):
            os.remove(backup_filename)
        with open(backup_filename, "w") as f:
            json.dump(modified_data, f, indent=2)        
        os.remove(filename)
        with open(filename, "w") as f:
            json.dump(modified_data, f, indent=2)

    def init(self) -> None:
        with open(filename, "w") as f:
            data = {
                "settings": {
                    "language": "en",
                    "currency": "USD",
                    "currency_symbol": "$",
                    "debug": True,
                },
                "delivery": {
                    "price": 0,
                    "enabled": False,
                },
                "checkout": {
                    "adress": True,
                    "phone": True,
                    "email": True,
                    "captcha": True,
                },
                "payment_methods": {
                    "cash": {
                        "title": "Cash",
                        "enabled": True,
                    },
                    "manager": {
                        "title": "Payment after contacting the manager",
                        "enabled": True,
                    },
                    "telegram_api": {
                        "title": "Payment via Telegram",
                        "enabled": False,
                    },
                  },
                "info": {
                    "greeting": "Welcome to our store!",
                    "contacts": "Phone: +7 (999) 999-99-99\nAddress: Moscow, Lenin street, 1",
                    "refund_policy": "Refund Policy",
                    "item_template": "Name: %n\nCategory: %c\nPrice: %p\n\nDescription: %d",
                },
            }
            json.dump(data, f, indent=2)
    
config = Config()


