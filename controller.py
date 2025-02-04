import sys
from typing import List
from database import create_tables, drop_tables
from process import run


def process_controller(script: str):
    if script == "process":
        run()

def db_controller(script: str):
    if script == "db_create_tables":
        create_tables()
    if script == "db_drop_tables":
        drop_tables()

def controller(cli_args: List[str]) -> None:
    groups = cli_args[1].split("_")
    group = groups[0]
    if group == "db":
        db_controller(script=cli_args[1])
    if group == "process":
        process_controller(script=cli_args[1])

if __name__ == "__main__":
    controller(sys.argv)