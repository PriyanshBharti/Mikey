import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Tanji.events import register
from Tanji import telethn as tbot


PHOTO = "https://telegra.ph/file/dcdbb6365975d066015c7.mp4"

@register(pattern=("/alive"))
async def awake(event):
    text = f"*👋 Hey There* {USER} \n\n"
    text += f"✨ *I'm {BOT_NAME}*\n🍀 *I'm Working Fine as always* \n\n"
    text += f"*👑 Owner:* [Devansh](tg://user?id=5288049130)\n"
    text += f"*💻 My Devs :* [Devs of {BOT_NAME}](https://t.me/SunBreatherUpdates/10)\n\n"
    text += "*⛅️ Bot version:* [Yorrichi 1.0](https://t.me/SunBreatherUpdates/)\n"
    text += "*🐍 Python-Telegram-Bot:*" + str(ptbver) + "\n"
    text += f"*⚡ Uptime:* {uptime}"
