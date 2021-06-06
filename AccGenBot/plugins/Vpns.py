import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"vpns"))
async def sed(event):
    text="I am an Account Generator Bot!\nI can generate working accounts for you.\n\nClick generate accounts to get your account!! Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.inline("Nord Vpn", data="nord"), Button.inline("Express Vpn", data="exv")],
                         [Button.inline("IpVanish", data="ips"), Button.inline("SurfShark", data="sfs")],
                         [Button.inline("Surfeasy VPN", data="sfv"), Button.inline("Windscribe", data="wnd")],
                         [Button.inline("Main Menu", data="start_bot"
                     ])
