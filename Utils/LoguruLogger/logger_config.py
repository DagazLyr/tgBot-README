from loguru import logger

dev_debug_output = "./Logs/dev_debug.log"
user_actions_loggs = "./Logs/user_action.log"
database_logger = "./Logs/Databases/MYSQL/driver.log"

def make_filter(name):
    def filter(record):
        return record["extra"].get("name") == name
    return filter

LOG_LEVEL_LENGTH = 9
log_formats = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <7}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"


logger.add(dev_debug_output, format = log_formats,
            level = "DEBUG", rotation = "00:00", compression="zip", filter=make_filter("development_debug"))

logger.add(user_actions_loggs, format=log_formats,
           level="INFO", rotation = "00:00", compression="zip", filter=make_filter("user_actions"))

logger.add(database_logger, format=log_formats,
           level="DEBUG", rotation = "100mb", compression="zip", filter=make_filter("mysql_log"))


debug_logger = logger.bind(name="development_debug")
user_logger = logger.bind(name="user_actions")
mysql_logger = logger.bind(name="mysql_log")