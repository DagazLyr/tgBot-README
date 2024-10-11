from ...imports import AsyncTeleBot
from ...Data import questions_cards_list

async def next_question_card(msg, bot: AsyncTeleBot):
    
    
    async with bot.retrieve_data(user_id=msg.user_id, chat_id=msg.chat_id) as user_data:
        q_index = user_data["question_index"]

        if "message_id" not in user_data:
            message = await bot.send_photo(
                chat_id = msg.chat_id,
                photo = questions_cards_list[q_index]['photo'],
                reply_markup = questions_cards_list[q_index]['reply_markup'])
            user_data["message_id"] = message.id
        else:
           
            message = await bot.edit_message_media(
                message_id=user_data["message_id"],
                chat_id=msg.chat_id,
                media=questions_cards_list[q_index]["e_photo"],
                reply_markup=questions_cards_list[q_index]["reply_markup"]
            )
        
        user_data["question_index"] += 1

    await bot.set_state(user_id=msg.user_id, state= questions_cards_list[q_index]['state'], chat_id=msg.chat_id)
