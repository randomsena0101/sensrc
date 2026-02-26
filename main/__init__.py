# Github.com/Vasusen-code

import logging, sys
from decouple import config
from pyrogram import Client as PyroClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

# ----------------------------
# Logging
# ----------------------------
logging.basicConfig(
    format='[%(levelname)5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

# ----------------------------
# Load configuration safely
# ----------------------------
from decouple import config

API_ID = config("API_ID", cast=int)           # 36905571
API_HASH = config("API_HASH")                 # 36677bbab05f148b95f91b13dbc57ea1
BOT_TOKEN = config("BOT_TOKEN")               # 8737801641:AAE7QoFn2deJt2WfTjVDt10hJGQow0wwgHA
SESSION = config("SESSION")                   # AQIzImMAI_Bzq8pvW5EtPvSvTfAfd4o7AFQd4CxBLf_KqDZMlLbcmHMPreQBjSh32nW6GctDwJcOsLBIYzgPw0P9RjOUv0wGUoOqfqxHASEV3sH_9xpez-J-TaDisZc8ILUwCXhfHOmES13sVPJA-D_rOkRolgZB5t0v-gmlD-54FfDqqYjHZZGy4plUGxVyEZrg2y3xhjWbAqTdQhvXKCjHUZ6Sy_MxmCtJ2SYeNmdjP3wpvgiU43Fog7AJ_dSGVWcjtaTs9eR-5G_R7N8WqoNxziamBEdgkxrZyizFt0tMZU3PJiMSgi8x3u1tEyX45lApMNcfitXorxGZtrOY0L5bsIKM-wAAAAHpC8m5AA
FORCESUB = config("FORCESUB", default="")    # aksjuatest
AUTH = config("AUTH", cast=int, default=0)   # 8204831161
# Validate critical credentials
if not all([API_ID, API_HASH, BOT_TOKEN]):
    print("Missing critical credentials (API_ID/API_HASH/BOT_TOKEN). Exiting.")
    sys.exit(1)

# ----------------------------
# Start Telethon userbot
# ----------------------------
try:
    userbot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
except Exception as e:
    print(f"Userbot init error: {e}")
    sys.exit(1)

async def start_userbot():
    try:
        await userbot.start()
        print("Userbot started!")
    except Exception:
        print("Userbot start failed! Check your SESSION string.")
        sys.exit(1)

# ----------------------------
# Start Pyrogram bot
# ----------------------------
bot = PyroClient(
    "SaveRestricted",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def start_bot():
    try:
        await bot.start()
        print("Bot started!")
    except Exception as e:
        print(f"Bot start failed: {e}")
        sys.exit(1)

# ----------------------------
# Main entrypoint
# ----------------------------
async def main():
    await asyncio.gather(start_userbot(), start_bot())
    print("Both bot and userbot are running!")
    await asyncio.Future()  # Keeps event loop alive

if __name__ == "__main__":
    asyncio.run(main())
