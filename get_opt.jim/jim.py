import pickle #-----------understood


def pack(response_dict):
    """produces message to send via tcp"""
    str_msg = pickle.dumps(response_dict)
    return str_msg #.encode("utf-8")


def unpack(byte_str):
    """unpacks received message"""
    str_decoded = pickle.loads(byte_str)#decode('utf-8')
    return str_decoded #return pickle.loads(str_decoded)


def status_200():
    msg = {
        "response": 200,
        "alert": "Optional message / notification"
    }
    return pack(msg)


def status_402():
    msg = {
        "response": 402,
        "error": "This could be wrong password or no account with that name"
    }
    return pack(msg)


def status_409():
    msg = {
        "response": 409,
        "alert": "Someone is already connected with the given user name"
    }
    return pack(msg)
