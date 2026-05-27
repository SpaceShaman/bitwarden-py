from .command_runner import run_command


def delete_item(password: str, item_id: str, permanent: bool = False) -> None:
    cmd = ["bw", "delete", "item", item_id]
    if permanent:
        cmd.append("--permanent")
    run_command(cmd, password=password)


def delete_folder(password: str, folder_id: str, permanent: bool = False) -> None:
    cmd = ["bw", "delete", "folder", folder_id]
    if permanent:
        cmd.append("--permanent")
    run_command(cmd, password=password)


def delete_attachment(password: str, attachment_id: str, item_id: str) -> None:
    run_command(
        [
            "bw",
            "delete",
            "attachment",
            attachment_id,
            "--itemid",
            item_id,
        ],
        password=password,
    )
