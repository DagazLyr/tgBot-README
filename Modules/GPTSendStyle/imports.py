from typing import List, Awaitable
from random import randint
from FletBot import AsyncTeleBot, MessageQuery, async_sleep
from FletBot.Markups import ReplyKeyboardMarkup, InlineKeyboardMarkup
from Modules.ResultType import ResultType, EnumStatuses
from FletBot import StatesGroup, State