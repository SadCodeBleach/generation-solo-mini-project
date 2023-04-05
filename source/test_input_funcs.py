from input_funcs import get_id_input
from unittest.mock import patch
import pytest


@patch('builtins.input')
def test_get_id_valid_int_input(mock_input):
    mock_input.return_value = 2
    
    expected = 2
    
    result = get_id_input(input_text=2)
    
    assert result == expected

 
@patch('builtins.print')   
@patch('builtins.input')
def test_get_id_invalid_str_input(mock_input, mock_print):
    mock_input.return_value = 'three'
    
    get_id_input(input_text='Insert Product ID: ')
    
    mock_print.assert_called_with('This is not an id!')
    

# @patch('builtins.input')
# def test_get_id_input_valid(mock_input):
#     mock_input.return_value = "2"
    
#     expected = 2
    
#     result = get_id_input()
    
#     assert expected == result

# test_get_id_input_valid()
