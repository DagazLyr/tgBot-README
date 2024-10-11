from setup import flet_bot, scheduller


#===========REGISTER_HANDLERS============#
#=====IMPORTS=====#
from Handlers.handlers import modules_handlers, bot_handlers
#=================#

#=====REGISTER=====#
flet_bot.registerHandlers(modules_handlers)
flet_bot.registerHandlers(bot_handlers)
#==================#
#========================================#



#===========REGISTER_SHEDULED_TASK============#
#=====IMPORTS=====#
#================SCHEDULE=================#

#=================#

#=====REGISTER=====#

#==================#
#============================================#