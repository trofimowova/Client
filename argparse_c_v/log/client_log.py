import logging

# install format: "<дата-время> <уровень_важности> <имя_модуля> <сообщение>"#
# объект форматирования
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Create FileHandlet to the log_file  "client.main.log" + encoding#
file_handler = logging.FileHandler("log/client.main.log", encoding="utf-8")
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create object of format#
client_logger = logging.getLogger("client.main")

# Add new handler and install logging level #
client_logger.addHandler(file_handler)
client_logger.setLevel(logging.DEBUG)


if __name__ == "__main__":

    client_logger.info("Тестовый запуск логирования")
    client_logger.warning("Тестовый запуск логирования")

    client_logger.setLevel(logging.WARNING)

    client_logger.debug("Тестовый запуск логирования")
    client_logger.critical("Тестовый запуск логирования")
