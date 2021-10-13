import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴜғᴏ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/75a6df41b61914b942b99.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/75a6df41b61914b942b99.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/75a6df41b61914b942b99.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/75a6df41b61914b942b99.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "italy_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "italy_music_1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ninjaaa_bots")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "update_music0")
OWNER_NAME = getenv("OWNER_NAME", "ITA_LYY") 
DEV_NAME = getenv("DEV_NAME", "ITA_LYY")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
