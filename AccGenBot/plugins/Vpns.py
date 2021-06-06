import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"vpns"))
button=[
    [Button.inline("Nord Vpn", data="nord"), Button.inline("Express Vpn", data="exv")],
    [Button.inline("IpVanish", data="ips"), Button.inline("SurfShark", data="sfs")],
    [Button.inline("Surfeasy VPN", data="sfv"), Button.inline("Windscribe", data="wnd")],
    [Button.inline("Main Menu", data="start_bot")]
])
