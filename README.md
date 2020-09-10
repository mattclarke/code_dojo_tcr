# code_dojo_tcr

## Setting up

### Create a virtual environment
Feel free to ignore if you already have a virtual environment configured or are using conda or are used to doing your own thing.
```
python3 -m venv .venv
. .venv/bin/activate
```

### Install some dependencies

```
python -m pip install -r requirements
```

### Opening the project in VS Code
```
code .
```

## Quick pytest primer

### Test examples
```
def test_example_of_an_equality_test():
    assert 2 + 2 == 4


def test_example_of_null_test():
    import time
    assert time.monotonic_ns() is not None
```

### Running the tests
```
pytest .
```

### Running the tests with coverage
```
pytest --cov .
```

