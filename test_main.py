def test_example_of_an_equality_test():
    assert 2 + 2 == 4


def test_example_of_null_test():
    import time
    assert time.monotonic_ns() is not None
