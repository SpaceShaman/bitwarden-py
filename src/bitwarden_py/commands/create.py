import json
from typing import Any

from .command_runner import run_command
from .encoding import encode


def create_item(password: str, item: dict[str, Any]) -> dict[str, Any]:
    output = run_command(["bw", "create", "item", encode(item)], password=password)
    return json.loads(output)


def create_folder(password: str, folder: dict[str, Any]) -> dict[str, Any]:
    output = run_command(["bw", "create", "folder", encode(folder)], password=password)
    return json.loads(output)


def create_attachment(password: str, file_path: str, item_id: str) -> dict[str, Any]:
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
