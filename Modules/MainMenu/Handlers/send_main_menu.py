from ..imports import *
from FletBot import call, CallbackQuery
from ..Markups import *
from telebot.types import InputMediaPhoto

@call
async def send_main_menu(call: CallbackQuery, bot: AsyncTeleBot):

    from ..States import MainMenuStates
    await bot.set_state(call.user_id, MainMenuStates.main_menu, call.chat_id)

    async with bot.retrieve_data(call.user_id, call.chat_id) as data:
        with open("Modules/MainMenu/Data/IMG/Main_menu.png", "rb") as img: 

            message_id = await bot.send_photo(
                photo=img,
                chat_id=call.chat_id,
                reply_markup=main_menu_markup
            )

            data["message_id"] = message_id