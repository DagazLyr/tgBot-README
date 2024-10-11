from ..imports import *
from FletBot import call, CallbackQuery
from requests import post
import json

@call
async def show_profile(call: CallbackQuery, bot: AsyncTeleBot): 

    data = {
        "id": call.chat_id
    }

    source = "http://94.79.43.195:8080/smallathone_product/hs/api/"

    response = post(url=f"{source}/leadinfo", data=json.dumps(data)).json()
    
    if len(response) == 0: 
        rating = "<b>Рейтинг:</b> <i>0</i>"
        tokens = "<b>Баллы:</b>: <i>0</i>"
        place  = "<b>Место:</b> <i>N</i>"
        grade  = "<b>Лига:</b> <i>Нет состоит в лиге</i>"
        tonextplace = "<b>До следующего места:</b>: N"
    else:
        rating = f"<b>Рейтинг:</b> <i>{response['rating']}</i>"
        tokens = f"<b>Баллы:</b>: <i>{response['tokens']}</i>"
        place  = f"<b>Место:</b> <i>{response['place']}</i>"
        grade  = f"<b>Лига:</b> <i>{response['grade']}</i>"
        tonextplace = f"<b>До следующего места:</b>: {response['tonextplace']}"

    text = f"<blockquote>{rating}\n{tokens}\n{place}\n{grade}\n{tonextplace}</blockquote>"

    await bot.send_message(
        chat_id=call.chat_id,
        text=text,
        parse_mode="HTML"
    )