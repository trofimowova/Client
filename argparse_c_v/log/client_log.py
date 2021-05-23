import logging

# формат лога: "<дата-время> <уровень_важности> <имя_модуля> <сообщение>"
_log_format = f'%(asctime)s - %(levelname)s - %(module)s - %(message)s '
# объект форматирования
formatter = logging.Formatter(_log_format)

# Создаем файловый обработчик логирования (можно задать кодировку)
# Журналирование должно производиться в лог-файл
file_handler = logging.FileHandler("log/client.main.log", encoding='utf-8')
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Создание именованного логгера
client_logger = logging.getLogger('client.main')

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
client_logger.addHandler(file_handler)
client_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    # проверяем
    client_logger.info('Тестовый запуск логирования')
    client_logger.warning('Тестовый запуск логирования')

    # Уровень логирования
    client_logger.setLevel(logging.WARNING)

    # Тест
    client_logger.debug('Тестовый запуск логирования')
    client_logger.critical('Тестовый запуск логирования')