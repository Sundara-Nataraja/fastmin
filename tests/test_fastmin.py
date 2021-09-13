import pytest

from fastmin.fastmin import __version__
from fastmin.fastmin.get_min import get_min
from fastmin.fastmin.exceptions import EmptyArray



def test_version():
    assert __version__ == '0.1.0'


def test_empty_array():
    arr = []
    with pytest.raises(EmptyArray):
        get_min(arr)


def test_simple_array():
    arr = [5, 4, 3, 2, 1, 3, 4, 5]
    assert get_min(arr) == min(arr)


def test_big_array():
    arr = list(range(1000, 5, -1)) + list(range(50000, 500000, 1))
    assert get_min(arr) == min(arr)


def test_very_big_array():
    arr = list(range(10 ** 6, 5, -1)) + list(range(50, 50 ** 4, 1))
    assert get_min(arr) == min(arr)


def test_array_withfloat():
    arr = [10.1, 9.2, 5.6, 5.9, 6.8, 7.9]
    assert get_min(arr) == min(arr)


def test_single_array():
    arr = [10]
    assert get_min(arr) == min(arr)


def test_two_array():
    arr = [10, 5]
    assert get_min(arr) == min(arr)


def test_only_increasing():
    arr = list(range(10 ** 6, 5, -1))
    assert get_min(arr) == min(arr)


def test_only_decreasing():
    arr = list(range(50, 50 ** 4, 1))
    assert get_min(arr) == min(arr)
