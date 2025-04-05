# python_cli_skeleton
a minimal working example of a properly packaged Python CLI program



## Installation

**from source**
```shell
$ python -m pip install git+https://github.com/neutrinoceros/python_cli_skeleton.git
```

or 
**install a dev copy in editable mode**
```shell
$ git clone ... # use https or ssh
$ cd python_cli_skeleton
$ python -m pip install -U --editable "."
```


## Test

from the root of the repo
```shell
$ python -m pip install pytest
$ pytest
```


## Demo

```shell
$ greet
Greeting Elvis !
```


## packaging: pyproject.toml

`pyproject.toml` is the central file that contains the package metadata.
It is where we define, for instance
- the version number
- the minimal Python requirement (`requires-python = ...`)
- runtime dependencies (`dependencies = ...`)
- the `greet` command (for more details see https://setuptools.pypa.io/en/latest/userguide/quickstart.html#entry-points-and-automatic-script-creation)


The package itself is organized as follow
```
.
├── LICENSE
├── README.md
├── pyproject.toml
├── skeleton
│   ├── __init__.py
│   └── __main__.py
└── tests
    └── test_greetings.py
```

- `skeleton` is the source directory (whose name matches that of the package, as declared in `pyproject.toml`). The presence of an `__init__.py` file makes it a Python package.
- the `__main__.py` module is where the code lives. This is also a special module name, which allows calling the main function from the command line in a different style:
```
$ python -m skeleton
Greetings Elvis !
```
