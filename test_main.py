import subprocess

def test_example_of_an_equality_test():
    assert 2 + 2 == 4


def test_example_of_null_test():
    import time
    assert time.monotonic_ns() is not None


def test_golden_master():
    result = subprocess.check_output(["python", "main.py"]).decode()
    with open("golden_master.txt") as f:
        golden_master = f.read()
    assert golden_master == result
