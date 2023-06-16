import pytest

# define a function to test
def calc_size(length, width, height, rounding=1):
    size = length * width * height
    size_rounded = round(size, rounding)
    return size_rounded


# define the tests, (the convention is to use "test_" for each tests function)

# test 1. 
def test_total_size():
    assert calc_size(10,10,10) == 1000
    assert calc_size(20, 10, 0.5) == 100

# test 2. 
def test_rounded():
    assert calc_size(1, 3.123, 10) == 31.2
    assert calc_size(1, 3.123, 10, rounding=2) == 31.23
