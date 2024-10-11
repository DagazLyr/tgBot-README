from FletBot import MessageHandler, CallbackHandler
from .States import BookSearchState
from .Handlers import *


question_commands_list = [
    MessageHandler(cmd_start, commands=['start'], pass_bot=True)
]

question_inline_list = [
    CallbackHandler(set_hero_props, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_hero_props),
    CallbackHandler(set_stroy_end,  func=lambda btn: True, pass_bot=True).set_state(BookSearchState.stroy_end),
    CallbackHandler(set_adaptation, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_adaptation),
    CallbackHandler(set_genre, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_genre),
    CallbackHandler(set_interests, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_interests),
    CallbackHandler(set_active_story, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_active_story),
    CallbackHandler(set_what_do_u_want, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_experience),
    CallbackHandler(set_setting, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_setting),
    CallbackHandler(set_pages_amount, func=lambda btn: True, pass_bot=True).set_state(BookSearchState.set_pages_amount),

    CallbackHandler(show_user_book, func=lambda btn: btn.data == "agree", pass_bot=True).set_state(BookSearchState.accept_policy),
    #CallbackHandler(ban_user, func=lambda btn: btn.data == "disagree", pass_bot=True).set_state(BookSearchState.accept_policy)
]

question_reply_list = [
    
]

question_handlers_list = [
    question_commands_list,
    question_inline_list,
    question_reply_list
]