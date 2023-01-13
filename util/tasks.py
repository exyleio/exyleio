from typing import Callable

import subprocess
import importlib.util
from os import system
from shutil import which
from multiprocessing import Process

from util.ansi import bold


def setup_firebase_cli() -> None:
    # install firebase CLI if it isn't installed already
    if which("firebase") is None:
        system("npm install -g firebase-tools")

    # logs-in to firebase if it hasn't already
    system("firebase login")


def get_module(module_name: str, script_path: str):
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def create_process(function: Callable) -> Process:
    """Create, start, and return a process"""

    process = Process(target=function)
    process.start()

    return process


def run_docker(services: list[str]) -> None:
    available_docker_compose_servicers = set(
        [
            s.decode("utf-8")
            for s in subprocess.run(
                "docker compose config --services".split(),
                stdout=subprocess.PIPE,
            ).stdout.split()
        ]
    )

    # only select valid docker compose services
    services = available_docker_compose_servicers.intersection(services)

    if len(services) == 0:
        print("no need to start docker compose. Skipping.")
        return

    command = f"docker compose up --build --remove-orphans --pull always {' '.join(services)}"  # noqa E501

    print(f"calling {bold(command)}")
    system(command)
