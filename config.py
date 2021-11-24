import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    PICS = os.environ.get("PICS", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    msg = {}
