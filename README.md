# code_dojo_tcr
```
cd code_dojo_tcr
```

## Setting up

### Create a virtual environment

Optional - Conda users or people who are happy to use the system Python can skip this.

```
python3 -m venv my_env
. my_env/bin/activate
```

### Install some dependencies

```
python -m pip install -r requirements.txt
```

### Opening the project in VS Code
```
code .
```

Check that the IDE has picked up the correct Python interpreter.

### Check tests run
```
pytest .
```


## Quick pytest primer

### Example tests
Simple comparisons

```
def test_example_of_an_equality_test():
    assert 2 + 2 == 4
```

```
def test_example_of_an_equality_test():
    my_list = [1, 2, 3]
    assert len(my_list) == 3
```

Testing for null:
```
def test_example_of_null_test():
    import time
    assert time.monotonic_ns() is not None
```


### Running the tests with coverage
```
pytest --cov .
```

