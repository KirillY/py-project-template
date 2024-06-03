# Python Project Template

[![Build Status](https://github.com/KirillY/py-project-template/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/KirillY/py-project-template/actions/workflows/python-ci.yaml)

This Python project template facilitates the setup and development of Python applications, using PDM (Python Dependency Manager) for effective dependency management. It includes robust pre-commit hooks to ensure code quality and consistency across contributions.

## Features
- **Dependency Management:** Simplified setup with PDM that supports separate environments for production and development.
- **Pre-commit Hooks:** Comes pre-configured with tools such as Ruff, Black, Mypy, and others for automated code formatting and linting.
- **Environment Variables:** Securely manage settings using `.env` files, which are kept out of source control for security.
- **Testing:** Integrated support for pytest to streamline running and writing tests.

## Getting Started
### Clone the Project
```shell
# Clone the repository into a directory of your choice
cd path/to/parent/directory
git clone https://github.com/KirillY/py-project-template.git <your-project-name>
cd <your-project-name>
```

### Install Dependencies
```shell
# Install production dependencies
pdm install --prod

# Install all dependencies for development
pdm install
```

### Configure Environment Variables
```shell
# Store environment variables securely
mkdir -p .env  # Create a directory for env files if it doesn't exist
echo "ENV_VARIABLE_NAME=value" > .env/<envname>.fenv
export $(cat .env/<envname>.env | xargs)
```

### Run Tests
```shell
# Run all tests
pdm run python -m pytest

# Run a specific test by name
pdm run python -m pytest -k test_name
```

### Use Pre-commit Hooks
```shell
# Apply pre-commit hooks to all files before committing
pdm run pre-commit run --all-files
```

## Detailed Installation & Configuration Guide
For more detailed instructions on setting up and configuring your local environment, refer to [this comprehensive guide](https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99).