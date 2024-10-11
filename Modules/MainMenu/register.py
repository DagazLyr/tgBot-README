from FletBot.Handlers import MessageHandler, CallbackHandler
from .Handlers.cmd_main_menu import cmd_send_main_menu
from .Handlers.show_profile import show_profile
from .Handlers.show_leadbooks import show_leadbooks
from .Handlers.start_test import start_test, to_answer

handlers_list = [
    MessageHandler(cmd_send_main_menu, commands=['main_meunu'], pass_bot=True),
    CallbackHandler(show_profile, func=lambda btn: btn.data == "profile", pass_bot=True),
    CallbackHandler(show_leadbooks, func=lambda btn: btn.data == "leadbooks", pass_bot=True),
    CallbackHandler(start_test, func=lambda btn: str(btn.data).startswith("test_"), pass_bot = True),
    CallbackHandler(to_answer, func=lambda btn: ((btn.data == "True") or (btn.data == "False")), pass_bot=True)
]