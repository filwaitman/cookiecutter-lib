# Cookiecutter lib

This is a bootstrap for creating a Python/Django lib with all the boilerplate for you:
* .gitignore
* .travis.yml
* LICENSE, MANIFEST.in
* README.md
* runtests.py
* setup.py, setup.cfg
* tox.ini

... so you can focus on what really matters: your piece of code. =]


# How to use it:

```bash
pip install cookiecutter
cookiecutter https://github.com/filwaitman/cookiecutter-lib
```


# Features:

* PyPI-ready;
* Integrated with TravisCI and Codecov services;
* Integrated with `tox` and `coverage` libs;
* Django support for lib creation. If, instead, you want the bootstrap for a complete Django project you should use [this](https://github.com/pydanny/cookiecutter-django);
* Python3 and Python2 support (but [you shouldn't use Python2, you know that](https://www.python.org/doc/sunset-python-2/)).


# TODO:

* Add tests
* Feature flags for py34 and py35
* Feature flags for TravisCI and Codecov
* Allow customization of license
