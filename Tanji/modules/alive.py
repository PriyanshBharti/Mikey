import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Tanji.events import register
from Tanji import telethn as tbot


PHOTO = "https://telegra.ph/file/6dec4385f44fc0af3ae67.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Mikey.** \n\n"
  TEXT += f"✯ **I'm Working Properly** \n\n"
  TEXT += f"✯ **Honorable Commander : [Commander](https://t.me/Darling_Hiro)** \n\n"
  TEXT += f"✯ **Library Version :** `{telever}` \n\n"
  TEXT += f"✯ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"✯ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/MikeySanoRobot?start=help"), Button.url("Support", "https://t.me/MikeySanosupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
