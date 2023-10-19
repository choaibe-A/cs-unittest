import pytest
from poetry_unittest import function
# Test cases

def test_integer_sort():
    input_list = [4, 6, 2, 2, 6, 4, 4, 4]
    expected_result = [4, 4, 4, 4, 6, 6, 2, 2]
    assert function.frequency_sort(input_list) == expected_result

def test_string_sort():
    input_list = ["bob", "bob", "carl", "alex", "bob"]
    expected_result = ["bob", "bob", "bob", "carl", "alex"]
    assert function.frequency_sort(input_list) == expected_result

def test_mixed_sort():
    input_list = [4, "bob", "carl", "bob", 4, "alex", 4]
    expected_result = [4, 4, 4, "bob", "bob", "carl", "alex"]
    assert function.frequency_sort(input_list) == expected_result

def test_empty_list():
    input_list = []
    expected_result = []
    assert function.frequency_sort(input_list) == expected_result

def test_single_element():
    input_list = [42]
    expected_result = [42]
    assert function.frequency_sort(input_list) == expected_result

# Run tests with pytest
if __name__ == "__main__":
    pytest.main()
