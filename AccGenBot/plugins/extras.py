import random
from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config
from dB import get_user_limit, add_user_to_db, get_all_users, dl_all_users, dl_one_user, add_hits_to_db, rm_all_hits, all_hit, rm_hit, hit_exists

@AccGenBot.on(events.NewMessage(pattern="/info"))
async def info(event):
    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**📡Your Account Information\n\nUser-ID : {event.sender_id}**")

@AccGenBot.on(events.NewMessage(pattern="/broad"))
async def reset(event):
    if event.sender_id != Config.OWNER_ID:
        return
    error = 0
    ds = event.text.split(" ", maxsplit=1)[1]
    ok = get_all_users()
    if not ok:
        await event.reply("Wut? No Users In Your Bot, But U Want To Broadcast. WTF")
        return
    for s in ok:
        try:
            await evil.send_message(int(s['user']), ds)
        except:
            error += 1
            pass
    await event.reply(f"Broadcast Done With {error} And Sucess in {len(ok) - error}!")    
        
async def clear_data():
    ok = get_all_users()
    if not ok:
        return
    for s in ok:
        try:
            await evil.send_message(int(s['user']), "**Limit Has Been Reset , Generate Your Accounts Now !**")
        except:
            error += 1
            pass
    dl_all_users()
