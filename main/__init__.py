#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "24894984" #config("API_ID", default=None, cast=int)
API_HASH = "4956e23833905463efb588eb806f9804" #config("API_HASH", default=None)
BOT_TOKEN = "7601293855:AAG0J1lG04wfEnK9J1GnImfOWN7X_2wyaS4" #config("BOT_TOKEN", default=None)
SESSION = "BQDNvmIAc2pCfy2TNwMsVQLUU3GjqNuJlYYq_mjlI6P06s6bwaXavLJwzSpREBdv2ckEr8oy-ZAk5FDVLW9EWqpee2b98CWmUDu2xq8kMveTugmPun9Y19IFNTc7d78Tc5NzAtjusgPETXDuUyxP7TIF25HDD6MyzfoRMJMNQNa7jtdMKehOSYdxged-mdYluK7PecGD62AL9NIuaat5H91UAdL8qyNqYjNlkRzi-C0BKBGIIn_MeHiQRK12QKe6Bv8E4DFHxi5wKS2DGYpr1foaVxgHmibV7ly1rZ2e-_6y-5A7COhAUTQvNF0sCCfsei3mS7T1kVgSy2Kun4QfE5xgRAJDQwAAAAA1y9g-AA" #config("SESSION", default=None)
FORCESUB = "Targetallcourse" #config("FORCESUB", default=None)
AUTH = "902551614" #config("AUTH", default=None)
SUDO_USERS = []

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
