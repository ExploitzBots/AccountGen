import random
from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/info"))
async def info(event):
    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**📡Your Account Information\n\nUser-ID : {event.sender_id}**")
