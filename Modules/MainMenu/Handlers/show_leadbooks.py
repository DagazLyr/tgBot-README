from ..imports import *
from FletBot import call, CallbackQuery
from requests import post
import json



@call
async def show_leadbooks(call: CallbackQuery, bot: AsyncTeleBot):

    print(1)
    data = {
        "id": call.chat_id
    }

    source = "http://94.79.43.195:8080/smallathone_product/hs/api/"

    response = post(url=f"{source}leadbooks/", data=json.dumps(data)).json()
    
    for book_data in response["books"]:
        
        print(book_data)

        book_id   = book_data["bookid"]
        book_name = book_data["name"]
        book_description = book_data["description"]
        read = book_data["read"]
        sheets = book_data["sheets"]

        import base64   
        image = base64.b64decode(book_data['preview'])
        
        from FletBot.Keyboards import ButtonBuilder
        from FletBot.Markups import MarkupBuilder

        test_markup = MarkupBuilder().inline().build().add(ButtonBuilder().inline().set_text("ПройдиТест").set_callback_data(f"test_{book_id}").build())

        await bot.send_photo(
            photo=image,
            chat_id=call.chat_id,
            reply_markup= test_markup if not read else None,
            caption = f"<blockquote><b><i>{book_name}</i></b>\n\n<b>Описание:</b>\n{book_description}\n<b>Можно пройти тест:</b> {"Да" if read else "Нет"}\n<b>Количество страниц:</b>{sheets}</blockquote>",
            parse_mode="HTML"
        )
    #text = f"<blockquote>{rating}\n{tokens}\n{place}\n{grade}\n{tonextplace}</blockquote>"