import json

from .command_runner import run_command
from .encoding import encode


def create_item(password: str, item: dict) -> dict:
    output = run_command(["bw", "create", "item", encode(item)], password=password)
    return json.loads(output)


def create_folder(password: str, folder: dict) -> dict:
    output = run_command(
        ["bw", "create", "folder", encode(folder)], password=password
    )
    return json.loads(output)


def create_attachment(password: str, file_path: str, item_id: str) -> dict:
    output = run_command(
        [
            "bw",
            "create",
            "attachment",
            "--file",
            file_path,
            "--itemid",
            item_id,
        ],
        password=password,
    )
    return json.loads(output)
