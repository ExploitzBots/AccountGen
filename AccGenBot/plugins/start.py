from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/start"))
async def start(event):

    await AccGenBot.send_message(Config.PRV_CHAT, f"Bot Started By [{event.sender_id}](tg://user?id={event.sender_id})")
    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.reply("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**Heya {name}\n\nWelcome To Premium Account Generator\n\nTry Command /help To Know More\n\nMade With ❤️ By @FreeCrackedHub**", buttons=[[Button.url("Join Channel!", Config.CHANNEL_URL)]])

#Repeat Codes :/
@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"start_bot"))
async def start(event):

    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.edit("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**Heya {name}\n\nWelcome To Premium Account Generator\n\nTry Command /help To Know More\n\nMade With ❤️ By @FreeCrackedHub**", buttons=[[Button.url("Join Channel!", Config.CHANNEL_URL)]])
