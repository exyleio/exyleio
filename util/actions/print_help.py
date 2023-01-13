from util.ansi import bold


def print_help() -> None:
    print(
        f"""
Usage:
  - must be called from where the script is located

  Clone repositories
    {bold('./tool.py clone')}

  Run projects and their dependencies
    {bold('./tool.py run <project1> <project2> <...>')}
    e.g.
      - {bold('./tool.py run api web docs')}
""",  # noqa E501
    )
