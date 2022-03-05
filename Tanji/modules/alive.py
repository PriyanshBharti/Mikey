import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Tanji.events import register
from Tanji import telethn as tbot


def alive(update: Update, context: CallbackContext):
    uptime = get_readable_time((time.time() - StartTime))
    first_name = update.effective_user.first_name
    USER = escape_markdown(first_name)
    text = f"*👋 Hey There* {USER} \n\n"
    text += f"✨ *I'm {BOT_NAME}*\n🍀 *I'm Working Fine as always* \n\n"
    text += f"*👑 Sun Breather:* [Devansh](tg://user?id=5288049130)\n"
    text += f"*💻 My Devs :* [Devs of {BOT_NAME}](https://t.me/SunBreatherUpdates/10)\n\n"
    text += "*⛅️ Bot version:* [Yorrichi 1.0](https://t.me/SunBreatherUpdates/)\n"
    text += "*🐍 Python-Telegram-Bot:*" + str(ptbver) + "\n"
    text += f"*⚡ Uptime:* {uptime}"
    update.effective_message.reply_animation(
      "CgACAgEAAx0CYCMspwACA7NiH1VUcTbiCRSvUFS6CmS6ZFUIlgACIgIAAqhPAUUBuE3Rfw7JbiME",
      caption=text,
      reply_markup=InlineKeyboardMarkup(group_buttons),
      parse_mode=ParseMode.MARKDOWN,
)
