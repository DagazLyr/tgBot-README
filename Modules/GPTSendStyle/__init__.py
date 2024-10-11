from Modules.GPTSendStyle.imports import *
from Modules.GPTSendStyle.entity_parser import *
from Modules.GPTSendStyle.states import StyleSenderStates

class EnumSendStatuses(EnumStatuses):
    INTERRUPT = "INTERRUPT"

class PartMessageSender:
    def __init__(self, message_time:float = 1.5,delay_coefficient: float = 0.07, smbl_per_part: int|None = None, end_sumbol: str = "...") -> None:
        self.delay_coef = delay_coefficient
        self.max_symbols = smbl_per_part
        self.__cached_texts = {}
        self.end_symbol = end_sumbol
        self.message_time = message_time


    def __set_symbols_from_text(self, text):
        return int((len(text))*3*0.14/self.message_time)


    async def flex_sleep(self):
        await async_sleep(randint(0,3)*self.delay_coef)


    def _render_text(self, text : str, cache_key : str|None = None) -> List[str]:
        if not (self.max_symbols):
            self.max_symbols = self.__set_symbols_from_text(text)

        rendered_parts_list = []
        format_tokens = []
        offset = 0
        pos = 0
        while pos < len(text):
            offset = get_text_part(text, pos+1, max_symbols_per_part=self.max_symbols)
            format_tokens = get_tokens_stack(text, format_tokens , start=pos, end=offset)
            rendered_parts_list.append(text[0:pos]+text[pos:offset]+get_tag_prefix_string(format_tokens[:]))
            pos = offset

        if (cache_key not in rendered_parts_list):
            self.__cached_texts[cache_key] = rendered_parts_list

        return rendered_parts_list


    async def __send_message(
            self, bot:AsyncTeleBot, send_func: Awaitable,
            max_symbols: int|None=None, cache_key : str|None = None,
            state:State|None=None, **kwargs)->ResultType: 
        
        if ("caption" in kwargs):
            type="caption"
            text = kwargs['caption']
        else:
            type="text"
            text = kwargs['text']

        self.max_symbols = self.__set_symbols_from_text(text)
        
        parts = []
        if (cache_key and cache_key in self.__cached_texts):
            parts = self.__cached_texts[cache_key]
        elif(cache_key):
            parts = self._render_text(text, cache_key)
        else:
            parts = self._render_text(text)

        await bot.set_state(kwargs['chat_id'], StyleSenderStates.wait_till_end, kwargs['chat_id'])
        for part in parts:
            try:
                usr_state = await bot.get_state(kwargs['chat_id'],kwargs['chat_id'])
                if (usr_state.__str__() != StyleSenderStates.wait_till_end.__str__()):
                    await bot.set_state(kwargs['chat_id'], state, kwargs['chat_id'])
                    await send_func(**kwargs)                    
                    return ResultType(EnumSendStatuses.INTERRUPT)
                kwargs[type]=part+self.end_symbol
                await send_func(**kwargs)   
                await self.flex_sleep()

            except Exception as _exp:
                pass

        await bot.set_state(kwargs['chat_id'], state, kwargs['chat_id'])
        kwargs[type]=text
        await send_func(**kwargs)
        return ResultType(EnumSendStatuses.SUCCESS)
    
    async def send_message_parts(
            self,
            bot:AsyncTeleBot,
            chat_id:int,
            message_id:int,
            text:str,
            state:State,
            reply_markup: ReplyKeyboardMarkup|InlineKeyboardMarkup|None=None,
            max_symbols:int|None=None,
            cache_key : str|None = None,
            **kwargs):
        
        parameters = {"chat_id": chat_id, "message_id": message_id, "bot":bot, "text":text, "state": state}
        if (reply_markup):           parameters["reply_markup"]= reply_markup
        if (max_symbols):            parameters["max_symbols"] = max_symbols
        if (cache_key):              parameters["cache_key"]   = cache_key
        if ("parse_mode" in kwargs): parameters["parse_mode"] = kwargs["parse_mode"]

        return await self.__send_message(send_func=bot.edit_message_text, **parameters)
    
    async def send_caption_parts(
            self,
            bot:AsyncTeleBot,
            chat_id:int,
            message_id:int,
            text:str,
            state:State,
            reply_markup: ReplyKeyboardMarkup|InlineKeyboardMarkup|None=None,
            max_symbols:int|None=None,
            cache_key : str|None = None,
            **kwargs):

        parameters = {"chat_id": chat_id, "message_id": message_id, "bot":bot, "caption":text,  "state": state}
        if (reply_markup):           parameters["reply_markup"]= reply_markup
        if (max_symbols):            parameters["max_symbols"] = max_symbols
        if (cache_key):              parameters["cache_key"]   = cache_key
        if ("parse_mode" in kwargs): parameters["parse_mode"] = kwargs["parse_mode"]

        return await self.__send_message(send_func=bot.edit_message_caption, **parameters)