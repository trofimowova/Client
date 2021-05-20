import argparse
import json
import sys
import select
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_configs, get_message, send_message, read_requests, write_responses
from log.server_log import server_logger
from log.log_decor import Log

CONFIGS = get_configs()

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
# функция проверки сообщения клиента
@Log("DEBUG")
def check_message(message):
    if (
        CONFIGS.get("ACTION") in message
        and message[CONFIGS.get("ACTION")] == CONFIGS.get("PRESENCE")
        and CONFIGS.get("TIME") in message
        and CONFIGS.get("USER") in message
        and message[CONFIGS.get("USER")][CONFIGS.get("ACCOUNT_NAME")] == "Trofimowova"
    ):
        server_logger.info("Cообщение клиента успешно проверено. Привет, клиент!")
        return {CONFIGS.get("RESPONSE"): 200, CONFIGS.get("ALERT"): "Привет, клиент!"}
    server_logger.error("Cообщение от клиента некорректно!")
    return {CONFIGS.get("RESPONSE"): 400, CONFIGS.get("ERROR"): "Bad request"}



# параметры командной строки скрипта server.py -p <port>, -a <addr>:
parser = argparse.ArgumentParser(description="command line server parameters")
parser.add_argument("-a", "--addr", type=str, default="", help="ip address")
parser.add_argument(
    "-p", "--port", type=int, default=CONFIGS.get("DEFAULT_PORT"), help="tcp-port"
)
args = parser.parse_args()
print(args)


def main():
    clients=[]
    # проверка параметров вызова ip-адреса и порта из командной строки
    try:
        if "-a" or "--addr" in sys.argv:
            listen_address = args.addr
            print(listen_address)
        else:
            listen_address = ""
    except IndexError:
        server_logger.critical("После '-a' - необходимо указать адрес")
        sys.exit(1)

    try:
        if "-p" or "--port" in sys.argv:
            listen_port = args.port
            print(listen_port)
        else:
            listen_port = CONFIGS.get("DEFAULT_PORT")
        if not 65535 >= listen_port >= 1024:
            raise ValueError
    except IndexError:
        server_logger.critical("После -'p' необходимо указать порт")
        sys.exit(1)
    except ValueError:
        # print("Порт должен быть указан в пределах от 1024 до 65535")
        server_logger.critical("Порт должен быть указан в пределах от 1024 до 65535")
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    # Bind to addr and port
    s.bind((listen_address, listen_port))
    # Ready to accept
    s.listen(CONFIGS.get("MAX_CONNECTIONS"))

    s.settimeout(1)

    while True:
        try:
            # принимает запрос на установку соединения
            client, addr = s.accept()
        except OSError as e:
            pass  # timeout вышел
        else:
            print(f'Получен запрос на соединение от {str(addr)}')
            clients.append(client)
        finally:
            r_list = []
            w_list = []
            try:
                r_list, w_list, e_list = select.select(clients, clients, [], 10)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r_list, clients, CONFIGS)  # Сохраним запросы клиентов
            if requests:
                print(requests)
                write_responses(requests, w_list, clients, CONFIGS)  # Выполним отправку ответов клиентам



if __name__ == "__main__":
    main()
