from functions import find_unique
import pytest


def test_basic_case():
    assert find_unique([1, 2, 3, 4, 3, 2, 1]) == 4


def test_negative_numbers():
    assert find_unique([-1, -2, -3, -8, -3, -2, -1]) == -8


def test_large_numbers():
    assert find_unique([10**6, 3, 10**6]) == 3


def test_single_element():
    assert find_unique([42]) == 42


def test_zero_included():
    assert find_unique([1, 1, 0, 2, 3, 3, 2]) == 0


def test_uneven_length():
    with pytest.raises(ValueError):
        assert find_unique([1, 2, 3, 1, 2, 3])
