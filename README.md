#WIP

###Roadmap:
- 🔴 Admin Panel
   * ~~Categories~~
     - ~~Addition~~
     - ~~Change~~
   * ~~Products~~
     - ~~Addition~~
     - ~~Change~~
   * ~~Users~~
     - ~~View Profile~~
     - ~~Change roles~~
   * Statistics
   * Settings
- ~~🗄️ Catalog~~
- 🛒 Shopping Cart
   * ~~Products~~
   * ~~Delivery~~
   * Checkout
- ~~📁 Profile~~
- ~~ℹ️ FAQ~~
- Payments
   * Manually
   * Telegram API
   * Qiwi/yoomoney?
- Readme

<hr>

# 🇬🇧Russian
# Why and who needs this bot?

Often, people who want to start a small online business do so through a social media profile, which requires them to manually process each application. This bot will allow everyone to quickly open an automated store based on a telegram bot, which will significantly reduce the order processing time.

# What is in the bot?
- The bot supports payment via payment systems (Telegram API).
- Admin panel for store management
     - Adding/changing/deleting a product
     - Add/change/delete categories
     - View/change user roles
     - Bot setup
     - Sales statistics with graphs and the ability to export to Excel.
- Product catalog with categories and subcategories
- Catalog search
- Shopping cart with the ability to choose the method of delivery and payment
- Personal account with order history
- FAQ with the ability to change questions and answers through the admin panel

# How to install?

The bot can be installed in two ways:
- [Docker(recommended)](#docker)
- [Manual installation](#manual)

##Docker

placeholder

##Manual
### Install dependencies

####Python 3.10

Windows:
```powershell
scoop install python # or install from the official site
```

Ubuntu:
```bash
sudo apt-get install python3.10 python3-pip
```

Fedora:
```bash
sudo dnf install python3.10 python3-pip
```

arch:
```bash
sudo pacman -S python3.10 python3-pip
```

Gentoo:
```bash
sudo emerge -av dev-lang/python:3.10 dev-python/pip
```

#### Poetry
Linux/MacOS/Windows(WSL):
```bash
curl -sSL https://install.python-poetry.org | python3-
```

Windows Powershell:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py-
```

### Bot installation

#### Clone the repository
```bash
git clone https://github.com/w1png/shop-telegram-bot
cd shop-telegram-bot
```

#### Create .env file
Linux/Macos:
```bash
touch.env
echo "TOKEN=token" >> .env
```

Windows:
```powershell
New-Item -Path .env -ItemType File
@echo off
echo "TOKEN=token" >> .env
```

#### Run the bot
```bash
install poetry # install dependencies and create a virtual environment
poetry run python3.10 src/__init__.py # start the bot
```