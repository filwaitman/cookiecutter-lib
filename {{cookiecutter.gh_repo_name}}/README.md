[![Build Status](https://travis-ci.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}.svg?branch=master)](https://travis-ci.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}})
[![codecov](https://codecov.io/gh/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}})

# {{cookiecutter.gh_repo_name}}

{{cookiecutter.short_description}}


## Example of basic usage:

TODO


## Features:

TODO


## Useful commands:

### Run linter:
```bash
pip install -r requirements_test.txt
isort -rc .
tox -e lint
```

### Run tests locally:
```bash
pip install -r requirements_test.txt
python runtests.py
```

### Run tests via `tox`:
```bash
pip install -r requirements_test.txt
tox
```

### Upload to PyPI:
```bash
pip install twine
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```


## FAQ:

TODO


## Contributing:

Please [open issues](https://github.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}/issues) if you see one, or [create a pull request](https://github.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}/pulls) when possible.
In case of a pull request, please consider the following:
- Respect the line length (132 characters)
- Keep the great test coverage of this project
- Run `tox` locally so you can see if everything is green (including linter and other python versions)


