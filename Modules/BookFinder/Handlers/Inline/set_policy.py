from ...imports import *
from ...Data import success_image
from FletBot import call, CallbackQuery
from ...Markups import agreement_markup


@call
async def set_policy(call: CallbackQuery, bot: AsyncTeleBot):

    async with bot.retrieve_data(call.user_id, call.chat_id) as user_data:
        message_id = user_data["message_id"]

    await bot.edit_message_media(
        media=success_image,
        chat_id=call.chat_id,
        message_id=user_data['message_id'],
        reply_markup=agreement_markup
    )

    from Modules.GPTSendStyle import PartMessageSender

    gpt_styler = PartMessageSender()
    await gpt_styler.send_caption_parts(
        bot,call.chat_id,
        message_id,"<blockquote>Для использования нашего сервиса примите согласие на <b>обработку персональных данных</b></blockquote>",
        state=BookSearchState.accept_policy,
        reply_markup=agreement_markup,
        parse_mode="HTML")
    