import json
import os
import sys

"""перевода сообщения из байтов"""
def get_message(opened_socket, CONFIGS):
    response = opened_socket.recv(CONFIGS.get('MAX_PACKAGE_LENGTH'))
    if isinstance(response, bytes):
        json_response = response.decode(CONFIGS.get('ENCODING'))
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError


"""перевода сообщения в байтов"""
def send_message(opened_socket, message, CONFIGS):
    json_message = json.dumps(message)
    response = json_message.encode(CONFIGS.get('ENCODING'))
    opened_socket.send(response)

"""получение словаря из json файла с настройками"""
def get_configs():
    if not os.path.exists('common/configs.json'):
        print('Файл конфигурации не найден')
        sys.exit(1)
    with open('common/configs.json') as configs_file:
        CONFIGS = json.load(configs_file)
        return CONFIGS

"""Чтение запросов из списка клиентов"""
def read_requests(r_clients, all_clients, CONFIGS):
    responses = {}
    for sock in r_clients:
        print(sock)
        print(r_clients)
        try:
            data = sock.recv(CONFIGS.get('MAX_PACKAGE_LENGTH')).decode(CONFIGS.get('ENCODING'))
            responses[sock] = data
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients, CONFIGS):
    # Эхо-ответ сервера клиентам, от которых были запросы

    for sock in w_clients:
        for _, request in requests.items():
            try:
                # Подготовить и отправить ответ сервера
                resp = request.encode(CONFIGS.get('ENCODING'))
                # Эхо-ответ сделаем чуть непохожим на оригинал
                sock.send(resp.upper())
            except:  # Сокет недоступен, клиент отключился
                print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
                sock.close()
                all_clients.remove(sock)