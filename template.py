import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
    ".github/workflows/ci.yaml",
    ".github/workflows/python-publish.yaml",
    ".gitignore",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_curd.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/ini.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    # making the file path with the system compatible like linux, windows etc...
    filepath = Path(filepath)
    # split the filedir and file from the path. filedir is the directory/ folder that we want to create.
    filedir, filename = os.path.split(filepath)
    # if the filedir is not empty then create a directory
    if filedir != "":
        # make the directory
        os.makedirs(filedir, exist_ok=True)

    # check if file path not exist othervise the size is zero
    if( not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

