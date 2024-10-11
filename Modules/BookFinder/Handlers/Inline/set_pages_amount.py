from ...imports import *
from .set_policy import set_policy
from FletBot import call, CallbackQuery

@call
async def set_pages_amount(call: CallbackQuery, bot: AsyncTeleBot):
    value = call.callback_data
    

    async with bot.retrieve_data(user_id=call.user_id, chat_id=call.chat_id) as user_data:
        user_data['pages_amount'] = int(value)
    
    await set_policy(call, bot)
