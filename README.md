# Python Project Template

[![Build Status](https://github.com/KirillY/py-project-template/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/KirillY/py-project-template/actions/workflows/python-ci.yaml)

This Python project template streamlines the setup and development of Python applications, utilizing PDM (Python Dependency Manager) for effective dependency management. It includes robust pre-commit hooks to ensure code quality and consistency across contributions.

## Features
- **Dependency Management:** Simplified setup with PDM supporting separate environments for production and development.
- **Pre-commit Hooks:** Comes pre-configured with tools such as Ruff, Black, Mypy, and others for automated code formatting and linting.
- **Environment Variables:** Secure management using `.env` files, kept outside of source control.
- **Testing:** Integrated pytest support for straightforward test execution.
- **Jupyter Integration:** In development mode, you can use Jupyter notebooks or VSCode to create `.ipynb` files for ad-hoc experiments. These files should be stored in a `notebooks/` directory that is excluded from version control.

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
# Install production dependencies (excludes Jupyter to speed up installation)
pdm install --prod

# Install all dependencies including Jupyter for development
pdm install
```

### Configure Environment Variables
```shell
# Securely store environment variables
mkdir -p .env  # Create a directory for env files if it doesn't exist
echo "ENV_VARIABLE_NAME=value" > .env/<envname>.env
export $(cat .env/<envname>.env | xargs)
```

### Experiment with Jupyter Notebooks
```shell
# Only in development mode
mkdir -p notebooks  # Create a directory for Jupyter notebooks if it doesn't exist
# Note: The notebooks/ directory is included in .gitignore to prevent version control
# You can use Jupyter or VSCode to create and manage `.ipynb` files
pdm run jupyter notebook
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

## Detailed Installation & Configurationz Guide
For more detailed instructions on setting up and configuring your local environment, refer to [this comprehensive guide](https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99).