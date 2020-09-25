import subprocess


def test_golden_master():
    result = subprocess.check_output(["python", "main.py"]).decode()
    with open("golden_master.txt") as f:
        golden_master = f.read()
    assert golden_master == result
