import getopt
import json
import sys
import pickle


def get_default_options(options_file):
    """get default program options from json file"""
    try:
        with open(options_file, "r") as f:
            config = pickle.load(f) #---------конфиг загружаем ДЖСОН
    except ValueError as err:
        print(f"Can`t read config file: {options_file}, with error: {err}") #----------обрабатываем ошибку
        sys.exit(2)#_____________________выход из системы
    return config


def get_command_line_options(args, cmd_line_opts):
    """get program options from command line"""
    try:
        opts, _ = getopt.getopt(args[1:], cmd_line_opts)#-----аргументы строки, ????- вот че это за хрень???Ы
    except getopt.GetoptError as err:
        print(f"Invalid argument value with error: {err}")
        sys.exit(2)
    return opts


def get_options(args, options_file):
    options = get_default_options(options_file)
    cl_options = get_command_line_options(args, "a:p:")
    for opt in cl_options:
        print("get port from options")
        if opt[0] == "-a":
            options['DEFAULT']['HOST'] = opt[1]#-----adreaa
        elif opt[0] == "-p":
            options['DEFAULT']['PORT'] = opt[1]#---port
    return options
