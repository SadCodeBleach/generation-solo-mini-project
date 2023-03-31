from input_funcs import get_id_input
from unittest.mock import patch
import pytest

def test_get_id_valid_input():
    
    expected = 1
    
    result = get_id_input(input_text='Select Product ID: ')
    
    assert expected == result
    



# @patch('builtins.input')
# def test_get_id_input_valid(mock_input):
#     mock_input.return_value = "2"
    
#     expected = 2
    
#     result = get_id_input()
    
#     assert expected == result

# test_get_id_input_valid()