from .logger_config import debug_logger, user_logger
import functools
from Modules.ResultType import *

def user_log(func=None, _message: str="USER_VOID"):

    def _decorate(function):
        
        @functools.wraps(function)
        async def wrap(*args, **kwargs):
            try:
                result_type = await function(*args, **kwargs)
                user_logger.info(f"function: {function.__name__}|{_message}|{result_type.__str__()}")
                return result_type
            except Exception as _ex:
                user_logger.error(f"function: {function.__name__}|{_message}" + f'{_ex}')
        return wrap
    
    if func:
        return _decorate(func)
    
    return _decorate

    
def debug_log(func=None, _message: str="DEBUG_VOID"):
    def _decorate(function):
        @functools.wraps(function)
        async def wrap(*args, **kwargs):
            try:
                result_type = await function(*args, **kwargs)
                debug_logger.debug(f"function: {function.__name__}|{_message}|{result_type.__str__()}")
                return result_type
            except Exception as _ex:
                debug_logger.debug(f"function: {function.__name__}|{_message}" + f'{_ex}')
        return wrap
    
    if func:
        return _decorate(func)
    
    return _decorate