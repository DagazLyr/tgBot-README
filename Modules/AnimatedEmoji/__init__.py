from FletBot import AsyncTeleBot, async_sleep

async def send_loading_with_success(chat_id, bot: AsyncTeleBot):
    temp_msg = await bot.send_message(
        chat_id=chat_id,
        text='⏳')
    await async_sleep(3)
    await bot.delete_message(
        chat_id=chat_id,
        message_id=temp_msg.id,
        timeout=1)
    

async def send_success_emoji(chat_id, bot: AsyncTeleBot):
    temp_msg = await bot.send_message(
        text="🎉",
        chat_id=chat_id)
    await async_sleep(3)
    await bot.delete_message(
        chat_id=chat_id,
        message_id=temp_msg.id,
        timeout=1)

