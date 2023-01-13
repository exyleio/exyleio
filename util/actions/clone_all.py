from os import system
from os.path import isdir

from util.constants import EXYLEIO_REPOSITORIES
from util.ansi import bold


def clone_all() -> None:
    """Clone repositories if it does not exist already."""

    print("Setting up projects...")
    print("  Cloning repositories...")

    for repo in [f"exyleio-{project}" for project in EXYLEIO_REPOSITORIES]:
        if isdir(repo):
            print(f"    Skipping {bold(repo)}. Already exists.")
            continue

        system(f"git clone https://github.com/exyleio/{repo}")
        print(f"    Cloned {bold(repo)}")

    print("Project setup complete!")
