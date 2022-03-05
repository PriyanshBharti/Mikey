import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Tanji.events import register
from Tanji import telethn as tbot

    uptime = get_readable_time((time.time() - StartTime))
    first_name = update.effective_user.first_name
    USER = escape_markdown(first_name)
    text = f"*👋 Hey There* {USER} \n\n"import os
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
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Ken Kaneki.** \n\n"
  TEXT += f"✯ **I'm Working Properly** \n\n"
  TEXT += f"✯ **My Owner : [⁰¹⁶ ᕼɪʀᴏ](https://t.me/Darling_Hiro)** \n\n"
  TEXT += f"✯ **Library Version :** `{telever}` \n\n"
  TEXT += f"✯ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"✯ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**⋨ Thanks For Adding Me Here**"
  BUTTON = [[Button.url("✢ Help ✢", "https://t.me/Kaneki_Ken_Robot?start=help"), Button.url("✢ Support ✢", "https://t.me/=KanekiSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

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
