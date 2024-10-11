from ...imports import *
from FletBot import msg, MessageQuery
from ..Reply.next_question_card import next_question_card
from ...States import BookSearchState


@msg
async def cmd_start(msg: MessageQuery, bot: AsyncTeleBot):

    await bot.set_state(user_id=msg.user_id, state=BookSearchState.init, chat_id=msg.chat_id)

    async with bot.retrieve_data(user_id=msg.user_id, chat_id=msg.user_id) as user_data:
        user_data = await set_book_search_user_data(user_data)

    await next_question_card(msg, bot)
