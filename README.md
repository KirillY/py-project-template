[![Build Status](https://github.com/KirillY/py-project-template/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/KirillY/py-project-template/actions/workflows/python-ci.yaml)
# Description

# Setup

### Install dependencies
- Production
```shell
cd /path/to/project/root
pdm install --prod
```
- Development
```shell
cd /path/to/project/root
pdm install
```


### Environment variables handling
- Store environment variables in the `<envname>.env` file
- Put the file into `.env` folder inside the project folder, ignored by git
- Alternatively, but `.env` file anywhere outsude the project folder
```shell
ENV_VARIABLE_NAME=value
```
- Export environment variables
```shell
export $(cat .env/<envname>.env | xargs)
```

### Comprehensive manual for Local Machine Installation & Configuration for a Python Testing Automation project
- https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99

# Run tests
```shell
cd /path/to/project/root
```
### Run all tests
```shell
pdm run python -m pytest
```

### Run selected test by name
```shell
pdm run python -m pytest -k test_name
```
# Pre-commit, Git hooks
- This Python template project leverages pre-commit hooks to ensure code quality and consistency. It includes tools like Ruff, Black, Mypy, Pydocstyle, Pyright, and general hooks for automatic code formatting and linting.
- To apply hooks:
  - make sure the pre-commit added to local git hooks
https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99#pre-commit-checks
  - before commiting, execute
```shell
pdm run pre-commit run --all-files
```