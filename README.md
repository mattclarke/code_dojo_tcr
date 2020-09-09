# code_dojo_tcr

## Setting up


Create a virtual environment.
Ignore if you already have a virtual environment configured or are using conda.
```
python3 -m venv .venv
. .venv/bin/activate
```

Install some dependencies:

```
python -m pip install -r requirements
```

## Quick pytest primer

Example tests:
```
def test_example_of_an_equality_test():
    assert 2 + 2 == 4


def test_example_of_null_test():
    import time
    assert time.monotonic_ns() is not None
```

Running the tests:
```
pytest
```

or
```
pytest test_main.py
```

## With coverage
```
pytest --cov .
```

