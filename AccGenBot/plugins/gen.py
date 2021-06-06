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
    [Button.inline("Vpn Section", data="vpns"), Button.inline("Streaming Section", data="str_sec")],
    [Button.inline("Main Menu", data="start_bot")]
vpns=[
  [Button.inline("Nord Vpn", data="nord"), Button.inline("IPVansih", data="ips")],
    [Button.inline("Main Menu", data="start_bot")]
    
])
