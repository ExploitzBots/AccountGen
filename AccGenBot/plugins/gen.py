import random
from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data="gen"))
async def gen(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.edit("**Join my channel for using this bot :)**", buttons=[[Button.url("Join Channel!", Config.CHANNEL_URL)]])
           return

    await event.edit("Choose Which Accounts you want to Generate", 
buttons=[
    [Button.inline("Vpn", data="Vpns"), Button.inline("Voot", data="voot")],
    [Button.inline("Wish", data="wish"), Button.inline("Shudder", data="shud")],
    [Button.inline("MeetMe", data="MeetMe"), Button.inline("Uplay", data="Uplay")],
    [Button.inline("Main Menu", data="start_bot")]
])

@AccGenBot.on(events.callbackquery.CallbackQuery(data="Vpns"))
async def gen(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.edit("**Join my channel for using this bot :)**", buttons=[[Button.url("Join Channel!", Config.CHANNEL_URL)]])
           return

    await event.edit("Select Your Option")
    buttons=[
        [Button.inline("IpVanish", data="IPS")],
        [Button.inline("NordVpn", data="Nord")]
    ])
   

