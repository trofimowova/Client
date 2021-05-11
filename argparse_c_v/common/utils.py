import json
import os
import sys
import pickle

# From bytes to DICT
def get_message(opened_socket, CONFIGS):
    response = opened_socket.recv(CONFIGS.get('MAX_PACKAGE_LENGTH'))
    if isinstance(response, bytes):
        #json_response = response.decode(CONFIGS.get('ENCODING'))
        response_dict = pickle.loads(response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError


"""Translate to bytes"""
def send_message(opened_socket, message, CONFIGS):
    json_message = pickle.dumps(message)
    #response = json_message.encode(CONFIGS.get('ENCODING'))
    opened_socket.send(json_message)

"""Get DICT_format from json_file"""
def get_configs():
    if not os.path.exists('common/configs.json'):
        print('Configuration file is not found')
        sys.exit(1)
    with open('common/configs.json') as configs_file:
        CONFIGS = json.load(configs_file)
        return CONFIGS