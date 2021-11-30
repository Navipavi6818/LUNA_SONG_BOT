import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from config import Config

BUTTONS = {}
SPELL_CHECK = {}

       
   @Client.on_message(filters.command('start'))
   async def start(client, message):
       buttons = [[                                    
            InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            InlineKeyboardButton('😊 About', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('🎧MUSIC🎧', callback_data='music'),
            InlineKeyboardButton('📀VSONG📀', callback_data='vsong')
            ],[
            InlineKeyboardButton('🎶LYRICS🎶', callback_data='lyrics')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('🤖 Updates', url='https://t.me/EvaMariaUpdates'),
            InlineKeyboardButton('♥️ Source', callback_data='source')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "source":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "music":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help'),           
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MUSIC,
            reply_markup=reply_markup,
            parse_mode='html'
        )            
    elif query.data == "vsong":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.VSONG,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "vsong":
        buttons = [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.LYRICS,
            reply_markup=reply_markup,
            parse_mode='html'
        )
