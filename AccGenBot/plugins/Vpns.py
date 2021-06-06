import random
from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data="vpns"))
async def vpns(vpns):

TEXT = """
**Heya {}**
Choose the account you wanna generate.
""".format(vpns.sender.first_name)

     await vpns.edit(TEXT, button=[
    [Button.inline("Nord Vpn", data="nord"), Button.inline("Express Vpn", data="exv")],
    [Button.inline("IpVanish", data="ips"), Button.inline("SurfShark", data="sfs")],
    [Button.inline("Surfeasy VPN", data="sfv"), Button.inline("Windscribe", data="wnd")],
    [Button.inline("Main Menu", data="start_bot")]
])
