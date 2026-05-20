import pytest
from app import divide


def test_divide():
    assert divide(10, 2) == 5.5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
