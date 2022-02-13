from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import LuciferMoringstar
from LuciferMoringstar_Robot.database.broadcast_db import Database

db = Database()


@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
                 InlineKeyboardButton("+ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜ'ʀᴇ Gʀᴏᴜᴘ +", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                 InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about") 
                 ],[
                 InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
                 ]]
        else:
            buttons = [[
                 InlineKeyboardButton("+ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜ'ʀᴇ Gʀᴏᴜᴘ +", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                 InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about") 
                 ],[
                 InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
                 ]]    
        await message.reply_photo(
            photo = choice(BOT_PICS),
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/b2acb2586995d0e107760.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_text(
            text=f"""<b>Hᴇʟʟᴏ {message.from_user.mention},

Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ</b>""",
            reply_markup=reply_markup
        )
        return
   
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    buttons = [[
              InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
              InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
              ],[
              InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
              ]]
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    buttons = [[
              InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
              InlineKeyboardButton("Hᴇʟᴘ", callback_data="help")
              ],[
              InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
              ]]  
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
