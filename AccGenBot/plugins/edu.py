import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"edu"))
async def happy(event):
    text="*Choose The Which Account You Want*"
    await event.edit(text,
                     buttons=[
                         [Button.inline("✘ KhanAcademy ✘", data="kha")],
                         [Button.inline("✘ UnAcademy ✘", data="una")],
                         [Button.inline("Main Menu", data="gen")]
                     ])
