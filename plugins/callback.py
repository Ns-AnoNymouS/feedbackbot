import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import feedback
from config import Config
from translation import Translation
from .commands import start 

@feedback.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

  if "feed" in cb_data:
      Config.feedback.append(m.from_user.id)
      button = [[InlineKeyboardButton("cancel", callback_data="cancel")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="Send your feed back here I will notify the admin.", reply_markup=markup)

  if "cancel" in cb_data:
      if m.from_user.id in Config.feedback:
         Config.feedback.remove(m.from_user.id)
      if m.from_user.id in Config.LOGIN:
         Config.LOGIN.remove(m.from_user.id)
      await m.message.delete()
      await start(c, m.message)

  if "rules" in cb_data:
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=Translation.RULES)

  if "login" in cb_data:
      Config.LOGIN.append(m.from_user.id)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=Translation.LOGIN)
       
  if "yes" in cb_data:
      Config.feedback.remove(m.from_user.id)
      feedtext = m.message.reply_to_message
      button = [[InlineKeyboardButton("Reply", callback_data=f"reply+{m.from_user.id}")]]
      markup = InlineKeyboardMarkup(button)
      for i in Config.OWNER:
          NS = await feedtext.forward(int(i))
          await NS.reply_text("Send the reply", reply_markup=markup, quote=True)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="Feedback sent successfully. Hope you will get reply soon")


  if "reply" in cb_data:
      id = m.data.split("+")[1]
      Config.SEND.append(id)
      await c.send_message(chat_id=m.message.chat.id, text="Reply me the text which you wantedto send him")

  if "about" in cb_data:
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=Translation.ABOUT, disable_web_page_preview=True)
