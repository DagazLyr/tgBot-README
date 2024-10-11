from...imports import *
from .send_main_menu import send_main_menu
from FletBot import msg, MessageQuery

async def cmd_send_main_menu(msg: MessageQuery, bot: AsyncTeleBot):
    await send_main_menu(msg, bot)