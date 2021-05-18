import logging
from logging.handlers import TimedRotatingFileHandler

# install format: "<дата-время> <уровень_важности> <имя_модуля> <сообщение>"#
# Create object of format#
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Create FileHandlet to the log_file  "server.main.log" + encoding#

file_handler = logging.FileHandler("log/server.main.log", encoding="utf-8")
file_handler.setFormatter(formatter)  # just like in line 5

# На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.!!!
time_rotating_handler = TimedRotatingFileHandler(
    "log/server.main.log", when="d", interval=1, backupCount=4, encoding="utf-8"
)
# file_handler.setLevel(logging.DEBUG)
time_rotating_handler.setFormatter(formatter)

# Create specific logger "server.main"#
server_logger = logging.getLogger("server.main")

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
# server_logger.addHandler(file_handler)
server_logger.addHandler(time_rotating_handler)
server_logger.setLevel(logging.DEBUG)

if __name__ == "__main__":

    server_logger.info("Testing log start")
    server_logger.warning("Testing log start")

    server_logger.setLevel(logging.WARNING)

    server_logger.debug("Testing log start")
    server_logger.critical("Testing log start")
