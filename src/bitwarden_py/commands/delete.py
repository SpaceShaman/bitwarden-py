from .command_runner import run_command


def delete_item(session: str, item_id: str, permanent: bool = False) -> None:
    cmd = ["bw", "delete", "item", item_id, "--session", session]
    if permanent:
        cmd.append("--permanent")
    run_command(cmd)


def delete_folder(session: str, folder_id: str, permanent: bool = False) -> None:
    cmd = ["bw", "delete", "folder", folder_id, "--session", session]
    if permanent:
        cmd.append("--permanent")
    run_command(cmd)


def delete_attachment(session: str, attachment_id: str, item_id: str) -> None:
    run_command(
        [
            "bw",
            "delete",
            "attachment",
            attachment_id,
            "--itemid",
            item_id,
            "--session",
            session,
        ]
    )
