import os
from pathlib import Path
import logging

# workflows folder: in this we are going to write
# the entire configuration of continuous integration(CI)
# continuous deployment(CD)
# we have stored a .gitkeep file inside this folder
# because github wont reflect the folder(.github folder as it is hidden) that
# is empty on its site when we run template.py and push the changes
# init_setup.sh : to intitalize the setup
# we write shell script, i.e. linux commands inside this file
# instead of writing it one by one, we unify the commnds
# and can directly run all of them together by just running the .sh file
# tox.ini : it is for testing diff cases
# in our local development environment


package_name = "mongodb_connect"

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "test/__init__.py",
    "test/unit/__init__.py",
    "test/unit/unit.py",
    "test/integration/__init__.py",
    "test/integration/integration.py",
    "init__setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
