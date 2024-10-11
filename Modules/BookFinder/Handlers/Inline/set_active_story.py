from ...imports import *
from ..Reply.next_question_card import next_question_card
from FletBot import call, CallbackQuery

@call
async def set_active_story(call: CallbackQuery, bot: AsyncTeleBot):
    value = call.callback_data

    async with bot.retrieve_data(user_id=call.user_id, chat_id=call.chat_id) as user_data:
        user_data['is_active_story'] = 4
    
    await next_question_card(call, bot)
