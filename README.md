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
# Install python3.10 from source

```bash
sudo apt-get update
sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
tar -xf Python-3.10.0.tgz
cd Python-3.10.0
./configure --enable-optimizations
make -j $(nproc)
sudo make altinstall
rm -r ../Python-3.10.0
rm Python-3.10.0.tgz
update-alternatives --install /usr/bin/python python3 /usr/local/bin/python3.10 10
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
#curl -sSL https://install.python-poetry.org | python3 -
curl -sSL https://install.python-poetry.org | python3.10 -
```

Windows Powershell:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
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
touch .env
echo "TOKEN=token" >> .env
echo "ADMIN_ID=admin_id" >> .env
```

Windows:
```powershell
New-Item -Path .env -ItemType File
@echo off
echo "TOKEN=token" >> .env
echo "ADMIN_ID=admin_id" >> .env
```

#### Run the bot
```bash
python3.10 -m venv venv
source venv/bin/activate
poetry install # install dependencies and create a virtual environment
poetry run python3.10 src/__init__.py # start the bot
```
