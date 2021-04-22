from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/start"))
async def start(event):

    await AccGenBot.send_message(Config.PRV_CHAT, f"Bot Started By [{event.sender_id}](tg://user?id={event.sender_id})")
    Soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if Soul is False:
            await event.reply("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"Heya {name}\n\nWelcome to AccGenBot, From Here You can Generate free Accounts\n\nMade With ❤️ By @ProAccountsHub", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

#Repeat Codes :/
@AccGenBot.on(events.callbackquery.CallbackQuery(data="start_bot"))
async def start(event):

    Soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if Soul is False:
            await event.edit("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.edit(f"Hoi ❤️ \n\nWelcome to AccGenBot, From Here You can Generate Accounts That You Want \n\nMade With ❤️ By @ProAccountsHub", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])
