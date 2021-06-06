import random
from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data="Vpns"))
async def gen(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.edit("**Join my channel for using this bot :)**", buttons=[[Button.url("Join Channel!", Config.CHANNEL_URL)]])
           return

    await event.edit("Choose Which Accounts you want to Generate", 
buttons=[
    [Button.inline("Nord Vpn", data="nord"), Button.inline("Express Vpn", data="exv")],
    [Button.inline("IpVanish", data="ips"), Button.inline("SurfShark", data="sfs")],
    [Button.inline("SurfeasyVPN", data="sfv"), Button.inline("Windscribe", data="wnd")],
    [Button.inline("Main Menu", data="start_bot")]
])
