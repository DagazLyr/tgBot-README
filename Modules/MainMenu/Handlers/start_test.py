from FletBot import call, CallbackQuery
from ..imports import *
from requests import post, put
import json

@call
async def to_answer(call: CallbackQuery, bot: AsyncTeleBot):
    value = call.callback_data

    async with bot.retrieve_data(call.user_id, call.chat_id) as data:

        await bot.edit_message_reply_markup(
            message_id = data["message_id"],
            chat_id= call.chat_id,
            reply_markup=None
        )
        
        data["correct"] += 1 if value=="True" else 0

        if len(data["tests_list"])<=0: 
            from .send_main_menu import send_main_menu

            put_data = {
                "lead": call.chat_id,
                "book": data["bookid"],
                "answers": data["correct"]
            }

            response = put(
                url="http://94.79.43.195:8080/smallathone_product/hs/api/booktest",
                data=json.dumps(put_data),
                headers = {'Content-Type': 'application/json'}
            ).json()

            message = f"<b>{response["message"]}</b>"
            rating  = f"<b>Рэйтинг:</b> <i>{response["rating"]}</i>"
            tokens  = f"<b>Баллы:</b> <i>{response["tokens"]}</i>"
            grade   = f"<b>Лига:</b> <i>{response["grade"]}</i>"


            await bot.send_message(
                chat_id=call.chat_id,
                text = f"Поздравляю!🎉\nКоличество правильных ответов: {data['correct']}\n<blockquote>{message}\n{rating}\n{tokens}\n{grade}</blockquote>",
                parse_mode="HTML"
            )

            await send_main_menu(call, bot)
            return None
        
        question = data["tests_list"].pop(0)
       

        text = f"<b>Вопрос:</b> {question['question']}"
        answers = question['answers']

        from FletBot.Markups import MarkupBuilder   
        from FletBot.Keyboards import ButtonBuilder

        markup = MarkupBuilder().inline().build()
        a_text = ""
        for i in range(len(answers)):
            a_text += f"{i+1}: {answers[i]['answer']}\n\n"
            markup.add(ButtonBuilder().inline().set_text(f"№-{i+1}").set_callback_data(f"{answers[i]['right']}").build())

        lst_msg = await bot.send_message(
            chat_id=call.chat_id,
            text= f"{text}\n{a_text}",
            reply_markup=markup,
            parse_mode="HTML"
        )   

        data["message_id"] = lst_msg.id

        
        

@call
async def start_test(call: CallbackQuery, bot: AsyncTeleBot):
    test_id = call.callback_data.split("_")[-1]
    
    data = {
        "id": test_id
    }

    response = post(
            url="http://94.79.43.195:8080/smallathone_product/hs/api/booktest",
            data=json.dumps(data),
            headers = {'Content-Type': 'application/json'}
    ).json()

    await bot.set_state(call.user_id, MainMenuStates.test, chat_id=call.chat_id)

    data_dict = response

    async with bot.retrieve_data(call.user_id, call.chat_id) as data:

        data.clear()
        data["bookid"]     = test_id,
        data["tests_list"] = data_dict['test']
        data["correct"]    = 0 

        question = data["tests_list"].pop(0)
        
        text = f"<b>Вопрос:</b> {question['question']}"
        answers = question['answers']

        from FletBot.Markups import MarkupBuilder   
        from FletBot.Keyboards import ButtonBuilder

        markup = MarkupBuilder().inline().build()
        a_text = ""
        for i in range(len(answers)):
            a_text += f"{i+1}: {answers[i]['answer']}\n\n"
            markup.add(ButtonBuilder().inline().set_text(f"№-{i+1}").set_callback_data(f"{answers[i]['right']}").build())

        lst_msg = await bot.send_message(
            chat_id=call.chat_id,
            text= f"{text}\n{a_text}",
            reply_markup=markup,
            parse_mode="HTML"
        )   

        data["message_id"] = lst_msg.id

