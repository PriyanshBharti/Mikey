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
async def alive(update: Update, context: CallbackContext):
    uptime = get_readable_time((time.time() - StartTime))
    first_name = update.effective_user.first_name
    USER = escape_markdown(first_name)
    KANEKI = f"👋 *Hey There* {USER} \n\n"
    KANEKI += f"✨ *I'm Kaneki*\n🍀 *I'm Working Fine as always* \n\n"
    KANEKI += f"👑* My Creator:* [Tamim](https://t.me/Darling_Hiro)"
    KANEKI += f"*🧑‍💻 My Devs :* [Devs of Kaneki](https://t.me/Shinobu_Update_Channel/34)\n\n"
    KANEKI += "*🧚‍♂️ Bot version:* [Kaneki 2.0](https://t.me/KanekiUpdates/7)\n"
    KANEKI += "*🐍 Python-Telegram-Bot:*" + str(ptbver) + "\n"
    KANEKI += f"*⚡ Uptime:* {uptime}"
    update.effective_message.reply_animation(
      ALIVE_PIC,
      caption=KANEKI,
      reply_markup=InlineKeyboardMarkup(group_buttons),
      parse_mode=ParseMode.MARKDOWN,
)
