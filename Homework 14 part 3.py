import pytest
from Homework_14 import Rectangle

rectangle_a = Rectangle(2, 3)
rectangle_b = Rectangle(5, 10)


def test_perimetr():
    assert rectangle_a.perimetr() == 10, 'Что то не то'


def test_equality():
    assert rectangle_a > rectangle_b == False, 'Что то не то'


if __name__ == '__main__':
    pytest.main()
