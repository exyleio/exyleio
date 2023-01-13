from types import ModuleType

from os import chdir, system
from os.path import dirname
from multiprocessing import Process

from util.ansi import bold
from util.tasks import (
    setup_firebase_cli,
    create_process,
    get_module,
    run_docker,
)


def run_deps(deps: set[str], processes: list[Process]) -> None:
    if "firebase" in deps:
        # setup firebase cli
        setup_firebase_cli()

        # start firebase emulator in the background
        processes.append(
            create_process(
                lambda: system("firebase emulators:start --only auth"),
            )
        )


def run_projects(
    projects: dict[str, ModuleType],
    processes: list[Process],
) -> None:
    for project_name in projects:
        # move into directory where scripts.py exists
        chdir(f"exyleio-{project_name}")

        # call scripts.pre()
        try:
            projects[project_name].pre()
        except AttributeError:
            pass

        # call scripts.run()
        def scripts_run():
            try:
                projects[project_name].run()
            except AttributeError:
                pass

        processes.append(create_process(scripts_run))

        # move back to exyleio master repo
        chdir("..")


def run(project_names: list[str]) -> None:
    print(f"  Running: {bold(', '.join(project_names))}")

    projects: dict[str, ModuleType] = dict()
    deps = set()
    processes: list[Process] = []

    for project_name in project_names:
        script_path = f"exyleio-{project_name}/scripts.py"

        try:
            project = get_module(project_name, script_path)
            projects[project_name] = project
        except FileNotFoundError:
            print(f"{bold(script_path)} does not exist")
            exit()

        # move into directory where scripts.py exists
        chdir(dirname(script_path))

        # collect dependencies
        try:
            deps.update(project.deps)
        except Exception:
            pass

        # move back to exyleio master repo
        chdir("..")

    run_deps(deps, processes)
    run_projects(projects, processes)
    run_docker(project_names)

    # join processes before terminating
    for process in processes:
        process.join()
