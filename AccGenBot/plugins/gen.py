import random
from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"gen"))
async def gen(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.edit("**Join my channel for using this bot :)**", buttons=[[Button.url("Join Channel!", Config.CHANNEL_URL)]])
           return

    await event.edit("Choose Which Accounts you want to Generate", 
buttons=[
    [Button.inline("✘ Vpn Accounts ✘", data="vpns")],
    [Button.inline("✘ Streaming Accounts ✘", data="stream")],
    [Button.inline("✘ P$RN Accounts ✘", data="porn")],
    [Button.inline("✘ Educational Accounts ✘", data="edu")],
    [Button.inline("Main Menu", data="gen")]
])
