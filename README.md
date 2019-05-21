# Python boilerplate project

[![Build Status](https://travis-ci.org/Akman/python-boilerplate.svg?branch=master)](https://travis-ci.org/Akman/python-boilerplate)
[![codecov](https://codecov.io/gh/Akman/python-boilerplate/branch/master/graph/badge.svg)](https://codecov.io/gh/Akman/python-boilerplate)
[![Requirements Status](https://requires.io/github/Akman/python-boilerplate/requirements.svg?branch=master)](https://requires.io/github/Akman/python-boilerplate/requirements/?branch=master)

A boilerplate project that exists as an aid to the [Python Packaging User
Guide][packaging guide]'s [Tutorial on Packaging and Distributing
Projects][distribution tutorial].

This project aims to cover best practices for Python project
development as a whole. It provides tool recommendations for linting and
testing.

[The source for this project is available here][src].

Most of the configuration for project is done in the `setup.py` file.
You should edit this file accordingly to adapt this boilerplate project
to your needs.

This is the README file for the project.

The file should use UTF-8 encoding and can be written using [markdown][md use]
with the appropriate [key set][md use]. It will be used to generate the project
webpage on PyPI and will be displayed as the project homepage on common
code-hosting services, and should be written for that purpose.

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not a
good idea, although a simple “What's New” section for the most recent version
may be appropriate.

All actions are performed from the project directory itself
where placed ***setup.py***

## Virtual environment

### Create virtual environment

```bash
$ python -m venv .venv
```

### Activate virtual environment

```bash
$ . .venv/Scripts/activate (Windows)
$ . .venv/usr/bin/activate (Linux)
```

### Deactivate virtual environment

```bash
$ deactivate
```

Further expected that virtual environment is **active**

## Install and update system packages

```bash
$ python -m pip install -U pip
$ python -m pip install -U setuptools
$ python -m pip install -U wheel
```

## Install package in editable mode

In *editable* mode, the package will not installed on the system,
and becomes available from the current directory. All changes in it
are immediately available and no need to reinstall it every time when
changes done.

```bash
$ python -m pip install -e .
```

### Install package in editable mode with development dependencies

See *extras_require.dev* in **setup.py**

Install flake8, pytest, tox, tox-venv, codecov and check-manifest packages.

```bash
$ python -m pip install -e .[dev]
```

## Lint

```bash
$ python -m flake8 .
```

## Test

```bash
$ python -m pytest
```

```bash
$ python -m codecov
```

## Manifest

```bash
$ check-manifest -v --ignore tox.ini,.editorconfig
```

## Automation

```bash
$ tox
```

## Run

### Console

```bash
$ python -m sample
$ python sample
$ sample_console
$ sample_script
```

### GUI

```bash
$ python -m sample --gui
$ python sample --gui
$ sample_gui
```

## Distribute

To create a source distribution

```bash
$ python setup.py sdist
```

To create a binary distribution

```bash
$ python setup.py bdist_wheel
```

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/Akman/python-boilerplate
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
