import json

from .command_runner import run_command
from .encoding import encode


def create_item(session: str, item: dict) -> dict:
    output = run_command(["bw", "create", "item", encode(item), "--session", session])
    return json.loads(output)


def create_folder(session: str, folder: dict) -> dict:
    output = run_command(
        ["bw", "create", "folder", encode(folder), "--session", session]
    )
    return json.loads(output)


def create_attachment(session: str, file_path: str, item_id: str) -> dict:
    output = run_command(
        [
            "bw",
            "create",
            "attachment",
            "--file",
            file_path,
            "--itemid",
            item_id,
            "--session",
            session,
        ]
    )
    return json.loads(output)
