from os import getenv
from dotenv import load_dotenv
from FletBot.felt_bot import FletBot

#==============LOADTOKENS================#
load_dotenv('./Configs/.env')

TELEGRAM_TOKEN = getenv("TEST_TOKEN_TELEGRAM")

#===============SETUPBOT=================#
flet_bot = FletBot(TELEGRAM_TOKEN)
flet_bot.addSheduller()
flet_bot.set_state_filter()

scheduller = flet_bot.scheduleManager

#================PAYMENT=================#

