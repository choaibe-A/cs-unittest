'''import modules'''

import sys
import os
import pytest
from poetry_unittest.function import frequency_sort

# Get the current script's directory and add the parent directory (project root) to sys.path
script_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
sys.path.append(project_root)


# Test cases

def test_integer_sort():
    '''
    test frequency_sort for integers
    '''
    input_list = [4, 6, 2, 2, 6, 4, 4, 4]
    expected_result = [4, 4, 4, 4, 6, 6, 2, 2]
    assert frequency_sort(input_list) == expected_result

def test_string_sort():
    '''
    test frequency_sort for strings
    '''
    input_list = ["bob", "bob", "carl", "alex", "bob"]
    expected_result = ["bob", "bob", "bob", "carl", "alex"]
    assert frequency_sort(input_list) == expected_result

def test_mixed_sort():
    '''
    test frequency_sort for mixed types
    '''
    input_list = [4, "bob", "carl", "bob", 4, "alex", 4]
    expected_result = [4, 4, 4, "bob", "bob", "carl", "alex"]
    assert frequency_sort(input_list) == expected_result

def test_empty_list():
    '''
    test frequency_sort for empty list
    '''
    input_list = []
    expected_result = []
    assert frequency_sort(input_list) == expected_result

def test_single_element():
    '''
    test frequency_sort for single element
    '''
    input_list = [42]
    expected_result = [42]
    assert frequency_sort(input_list) == expected_result

# Run tests with pytest
if __name__ == "__main__":
    pytest.main()
