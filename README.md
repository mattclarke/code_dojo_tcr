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

### Install dependencies

```
python -m pip install -r requirements.txt
```

### Check tests run

```
pytest .
```

## test && commit || revert
[Kent Beck's original article](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864)

After every change we run the tests via "test && commit || revert", if they pass then the change is committed but if they fail then the code is reverted to the state it was in when the tests last passed.

The (artifical) aim is to keep the test coverage at 100%, i.e. writing implementation code should be followed immediately by writing test code for it (or vice versa). Then it is time to "test && commit || revert" it.

"test && commit || revert" should be run at least every few minutes.

The real command for doing "test && commit || revert" with pytest and git is:
```
pytest --cov .  && git commit -am working || git reset --hard
```

NOTE: it is possible to cheat and retrieve code even after it has been reverted, please don't do this - not even for a typo!

### PyCharm - auto test && commit || revert
Create a shell script called tcr.sh and add the following to it:
```
pytest --cov .  && git commit -am working || git reset --hard
```
"test && commit || revert" can then be added as an external tool via `Preferences->Tools`.
The settings are:
* Program = sh
* Arguments = tcr.sh

Via `Preferences->Tools` it is also possible to add a keyboard shortcut.


### VS Code - auto test && commit || revert
It is pretty simple to set up VS Code to automatically TCR on saving. First, install the "Run on Save" plugin by pucelle. Then open the settings.json file and add the following:
```
    "runOnSave.commands": [
        {
            "match": ".*\\.py$",
            "command": "workbench.action.files.saveAll",
            "runIn": "vscode"
        },
        {
        "match": ".*\\.py",
        "command": "clear; pytest --cov .  && git commit -am working || git reset --hard",
        "runIn": "terminal"
        }
    ]
```
Finally, from `Preferences` turn `Auto Save` off.
Now the "test && commit || revert" command will be run  automatically on saving.

## Quick pytest primer

### Example tests
Simple comparisons:

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

