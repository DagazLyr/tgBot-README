from ...imports import *
from ..Reply.next_question_card import next_question_card
from FletBot import call, CallbackQuery

@call
async def set_adaptation(call: CallbackQuery, bot: AsyncTeleBot):
    value = call.callback_data

    async with bot.retrieve_data(user_id=call.user_id, chat_id=call.chat_id) as user_data:
        user_data['has_adaptation'] = 10 if (value == "yes") else 0
    
    await next_question_card(call, bot)
