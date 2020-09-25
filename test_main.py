import subprocess
import pytest_check as check


def test_golden_master():
    result = subprocess.check_output(["python", "main.py"]).decode()
    with open("golden_master.txt") as f:
        golden_master = f.read()

    result = result.split("\n")
    golden_master = golden_master.split("\n")

    for res, gold in zip(result, golden_master):
        check.equal(res, gold)
