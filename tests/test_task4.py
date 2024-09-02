from task4.task4 import find_min_moves_to_equal_elements
import pytest


def test__find_min_moves_to_equal_elements__nums_is_empty():
    with pytest.raises(IndexError):
        assert find_min_moves_to_equal_elements([])


def test__find_min_moves_to_equal_elements__nums_is_not_empty():
    assert find_min_moves_to_equal_elements([1, 2, 3]) == 2