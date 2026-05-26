import json

from .command_runner import run_command
from .encoding import encode


def edit_password(session: str, item_name: str, new_password: str) -> None:
    item = json.loads(
        run_command(["bw", "get", "item", item_name, "--session", session])
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
            "--session",
            session,
        ]
    )


def edit_item(session: str, item_id: str, item: dict) -> dict:
    output = run_command(
        ["bw", "edit", "item", item_id, encode(item), "--session", session]
    )
    return json.loads(output)


def edit_folder(session: str, folder_id: str, folder: dict) -> dict:
    output = run_command(
        ["bw", "edit", "folder", folder_id, encode(folder), "--session", session]
    )
    return json.loads(output)
