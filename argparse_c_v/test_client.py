
from client import check_response
from common.utils import get_configs
import pytest




CONFIGS = get_configs()

test_error_message = f'400: Bad request'
test_correct_message = f'200: OK, Привет, клиент!'

def test_error_response():
    assert (check_response({
        CONFIGS.get('RESPONSE'): 400,
        CONFIGS.get('ERROR'): 'Bad request',
    })== test_error_message)

def test_correct_response():
    assert (check_response({
        CONFIGS.get('RESPONSE'): 200,
        CONFIGS.get('ALERT'): 'Привет, клиент!'
    })==test_correct_message)

def test_no_response():
    with pytest.raises(ValueError):
     check_response({CONFIGS.get('ERROR'): 'Bad request'})

if __name__ == '__main__':
    pytest.main()