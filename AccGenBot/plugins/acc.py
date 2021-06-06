from . import *
from .. import *
from Configs import Config
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
import random
from lists import users




@AccGenBot.on(events.callbackquery.CallbackQuery(data="zee5"))
async def zee5(event):
    chat = event.sender_id
    soul = await verify(Config.CHANNEL_US, event, AccGenBot)


    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return
    try:
        if users[chat]:
            users[chat] += 1
    except:
        users[chat] = 1

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    if users[chat] <= 10:
        with open('zee5.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**Zee5 Account**\n\nCombo: {email}:{password}\nEmail: {email}\nPassword: {password}\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nLimit Remained= {5-users[chat]}",
    buttons=[
        [Button.url("Join Channel", Config.CHANNEL_URL)],
        [Button.inline("Generate Again", data="gen")]
    ])
    else:
        await hehe.edit("Limit Exceed")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="voot"))
async def voot(event):
    chat = event.sender_id
    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    try:
        if users[chat]:
            users[chat] += 1
    except KeyError:
        users[chat] = 1
    if users[chat] <= 10:
        with open('voot.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**Voot Account**\n\nCombo: {email}:{password}\nEmail: {email}\nPassword: {password}\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nLimits Remained = {5-users[chat]}",
    buttons=[
        [Button.url("Join Channel", Config.CHANNEL_URL)],
        [Button.inline("Back", data="gen")]
    ])
    else:
        await hehe.edit("LIMIT EXCEED")

@AccGenBot.on(events.callbackquery.CallbackQuery(data="wish"))
async def wish(event):
    chat = event.sender_id
    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")
    try:
        if users[chat]:
            users[chat] += 1
    except KeyError:
        users[chat] = 1


    if  10 >= users[chat]:
        with open('wish.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**Wish Account**\n\nCombo: {email}:{password}\nEmail: {email}\nPassword: {password}\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nLimits Remained= {5-users[chat]}",
    buttons=[
        [Button.url("Join Channel", Config.CHANNEL_URL)],
        [Button.inline("Back", data="gen")]
    ])
    else:
        hehe.edit("LIMIT EXCEED")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="shud"))
async def shud(event):
    chat = event.sender_id
    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")
    try:
        if users[chat]:
            users[chat] += 1
    except KeyError:
        users[chat] = 1
    if 10>= users[chat]:

        with open('shud.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**Shudder Account**\n\nCombo: {email}:{password}\nEmail: {email}\nPassword: {password}\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nREST OF LIMIT {5-users[chat]}",
    buttons=[
        [Button.url("Join Channel", Config.CHANNEL_URL)],
        [Button.inline("Back", data="gen")]
    ])
    else:
        await hehe.edit("LIMIT EXCEED")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="MeetMe"))
async def MeetMe(event):
    chat = event.sender_id
    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")
    try:
        if users[chat]:
            users[chat] +=1
    except KeyError:
        users[chat] = 1
    if 10 >= users[chat]:

        with open('MeetMe.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**MeetMe Account**\n\nCombo: {email}:{password}\nEmail: {email}\nPassword: {password}\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nREST OF LIMITS {10-users[chat]}",
buttons=[
    [Button.url("Join Channel", Config.CHANNEL_URL)],
    [Button.inline("Back", data="gen")]
])
    else:
        await hehe.edit("LIMIT EXCEED")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="Uplay"))
async def uplay(event):
    chat = event.sender_id
    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")
    try:
        if users[chat]:
            users[chat] +=1
    except KeyError:
        users[chat] = 1
    if 10 >= users[chat]:
        with open('Uplay.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**Uplay Account**\n\nCombo: {email}:{password}\nEmail: {email}\nPassword: {password}\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nREST IF LIMIT = {10-users[chat]}",
    buttons=[
        [Button.url("Join Channel", Config.CHANNEL_URL)],
        [Button.inline("Back", data="gen")]
    ])
    else:
        await hehe.edit("LIMIT EXCEED")

@AccGenBot.on(events.callbackquery.CallbackQuery(data="Vpns"))
    buttons=[
        [Button.inline("IpVanish", data="IPS")],
        [Button.inline("NordVpn", data="Nord")]
    ])
    else:
        await hehe.edit("Limit Over")
