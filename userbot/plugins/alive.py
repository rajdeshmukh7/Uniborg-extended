"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`𝕀 𝕒𝕞 𝕒𝕝𝕚𝕧𝕖 𝕞𝕪 𝕞𝕒𝕤𝕥𝕖𝕣`**\n\n"
                     "`𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: 6.9.0\nPython: 3.7.3\n\n"
                     "`𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝘀𝘁𝗮𝘁𝘂𝘀: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`𝗠𝘆 𝗣𝗲𝗿𝘂 𝗼𝘄𝗻𝗲𝗿`: {DEFAULTUSER}\n")
