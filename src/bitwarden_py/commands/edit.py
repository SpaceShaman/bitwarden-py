import json

from .command_runner import run_command
from .encoding import encode


def edit_password(password: str, item_name: str, new_password: str) -> None:
    item = json.loads(
        run_command(["bw", "get", "item", item_name], password=password)
    )

    if not item.get("login"):
        raise RuntimeError(f"Item '{item_name}' is not a login item")

    item["login"]["password"] = new_password

    run_command(
        [
            "bw",
            "edit",
            "item",
            item["id"],
            encode(item),
        ],
        password=password,
    )


def edit_item(password: str, item_id: str, item: dict) -> dict:
    output = run_command(
        ["bw", "edit", "item", item_id, encode(item)], password=password
    )
    return json.loads(output)


def edit_folder(password: str, folder_id: str, folder: dict) -> dict:
    output = run_command(
        ["bw", "edit", "folder", folder_id, encode(folder)], password=password
    )
    return json.loads(output)
