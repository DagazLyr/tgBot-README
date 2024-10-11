from ...imports import *
from ..Reply.next_question_card import next_question_card
from FletBot import call, CallbackQuery

@call
async def set_stroy_end(call: CallbackQuery, bot: AsyncTeleBot):
    value = call.callback_data

    async with bot.retrieve_data(user_id=call.user_id, chat_id=call.chat_id) as user_data:
        user_data['stroy_end'] = 10 if (value == "yes") else 0  
    
    await next_question_card(call, bot)
