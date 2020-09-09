from main import fizz_buzz

def test_example_of_an_equality_test():
    assert 2 + 2 == 4


def test_example_of_null_test():
    import time
    assert time.monotonic_ns() is not None


def test_fizz_buzz_of_one():
    assert fizz_buzz(1) == 1


def test_fizz_buzz_of_three():
    assert fizz_buzz(3) == "fizz"


def test_fizz_buzz_of_five():
    assert fizz_buzz(5) == "buzz"


def test_fizz_buzz_of_two():
    assert fizz_buzz(2) == 2
