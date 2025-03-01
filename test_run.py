from kaushiksmess import *
import pytest

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_float():
    with pytest.raises(ValueError):
        factorial(2.5)

def test_factorial_string():
    with pytest.raises(ValueError):
        factorial("abc")


def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_positive():
    assert fibonacci(5) == 5

def test_fibonacci_negative():
    with pytest.raises(TypeError):
        fibonacci(-1)

def test_fibonacci_float():
    with pytest.raises(TypeError):
        fibonacci(2.5)

def test_fibonacci_string():
    with pytest.raises(TypeError):
        fibonacci("abc")


if __name__ == "__main__":
    pytest.main()