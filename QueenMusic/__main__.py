import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from QueenMusic import LOGGER, app, userbot
from QueenMusic.core.call import Alexa
from QueenMusic.plugins import ALL_MODULES
from QueenMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("QueenMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("QueenMusic.plugins" + all_module)
    LOGGER("QueenMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Alexa.start()
    try:
        await Alexa.stream_call("https://telegra.ph//file/6b43736232114415e3564.jpg")
    except NoActiveGroupCall:
        LOGGER("QueenMusic").error(
            "[ERROR] - \n\nHey Baby, Turn on voice chat or else will kill you. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Alexa.decorators()
    LOGGER("QueenMusic").info("FALL IN LOVE ❣️")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("QueenMusic").info("Stopping Music Bot, suma irudaa baka (Gaana pattu)")
