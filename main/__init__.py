#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
heroku config:set API_ID=36905571
heroku config:set API_HASH="36677bbab05f148b95f91b13dbc57ea1"
heroku config:set BOT_TOKEN="8737801641:AAE7QoFn2deJt2WfTjVDt10hJGQow0wwgHA"
SESSION = config("SESSION", default=None)
ORCESUB = config("FORCESUB", default="aksjuatest")
AUTH = config("AUTH", default=8204831161, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
