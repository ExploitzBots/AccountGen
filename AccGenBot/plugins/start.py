from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/start"))
async def start(event):

    await AccGenBot.send_message(Config.PRV_CHAT,"Bot Started By [{event.sender_id}](tg://user?id={event.sender_id})")
    Soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if Soul is False:
            await event.reply("**Sad , Dude 🥺 Join Channel To Use :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = sender.user.first_name
    await event.reply("Heya {name}\n\nWelcome to Boi 🔥, From Here You can Generate Premium Accounts\n\nMade With ❤️ By @ExploitzBots", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

#Repeat Codes :/
@AccGenBot.on(events.callbackquery.CallbackQuery(data="start_bot"))
async def start(event):

    Soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if Soul is False:
            await event.edit("**Join My channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = sender.user.first_name
    await event.edit("Heya {name}\n\nWelcome to AccGenBot, From Here You can Generate free Accounts\n\nMade With ❤️ By @ExploitzBots", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])
