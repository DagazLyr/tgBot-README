from ...imports import *
from FletBot import call, CallbackQuery
from PIL import Image
import io
from io import BytesIO
import base64

import json
from requests import put


@call
async def show_user_book(call: CallbackQuery, bot: AsyncTeleBot):

    

    async with bot.retrieve_data(call.user_id, call.chat_id) as data:
        print(data)

        put_data = {
            "id":           call.user_id,
            "login":        call.username,
            "age":          20,
            "kindness":     data['hero_props'],
            "ended":        data['stroy_end'],
            "film":         data['has_adaptation'],
            "genre":        data['genre'],
            "dynamic":      data['genre'],
            "expectations": data['experience'],
            "satting":      data['setting'],
            "sheets":       data['pages_amount'],
        }
        json_dumps = json.dumps(put_data)

        response = put(
            url="http://94.79.43.195:8080/smallathone_product/hs/api/lead/",
            data=json_dumps,
            headers = {'Content-Type': 'application/json'}
        ).json()

        book_name = response["name"]
        book_description = response["description"]
        message_id = data["message_id"]

    from telebot.types import InputMediaPhoto    
    image = InputMediaPhoto(base64.b64decode(response['preview']))

    await bot.edit_message_media(
        media=image,
        chat_id=call.chat_id,
        message_id=message_id,            
    )

    await bot.edit_message_caption(
        message_id=message_id,
        chat_id=call.chat_id,
        caption = f"<blockquote><b><i>{book_name}</i></b>\n\n<b>Описание:</b>\n{book_description}</blockquote>",
        parse_mode="HTML"
    )
    
    from Modules.MainMenu.Handlers import send_main_menu
    await send_main_menu(call, bot)