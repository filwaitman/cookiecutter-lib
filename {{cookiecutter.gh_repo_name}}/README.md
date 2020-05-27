[![Build Status](https://travis-ci.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}.svg?branch=master)](https://travis-ci.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}})
[![codecov](https://codecov.io/gh/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}})

# {{cookiecutter.gh_repo_name}}

{{cookiecutter.short_description}}


## Development:

### Run linter:
```bash
pip install -r requirements_dev.txt
isort -rc .
tox -e lint
```

### Run tests via `tox`:
```bash
pip install -r requirements_dev.txt
tox
```

### Release a new major/minor/patch version:
```bash
pip install -r requirements_dev.txt
bump2version <PART>  # <PART> can be either 'patch' or 'minor' or 'major'
```

### Upload to PyPI:
```bash
pip install -r requirements_dev.txt
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```

## Contributing:

Please [open issues](https://github.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}/issues) if you see one, or [create a pull request](https://github.com/{{cookiecutter.gh_username}}/{{cookiecutter.gh_repo_name}}/pulls) when possible.
In case of a pull request, please consider the following:
- Respect the line length ({{cookiecutter.line_length}} characters)
- Write automated tests
- Run `tox` locally so you can see if everything is green (including linter and other python versions)
