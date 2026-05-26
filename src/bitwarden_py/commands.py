import base64
import json
import os
from dataclasses import dataclass
from typing import Literal

from .command_runner import run_command


@dataclass
class Status:
    status: Literal["locked", "unlocked", "unauthenticated"]
    server_url: str


def get_status() -> Status:
    output = run_command(["bw", "status"])
    status_data = json.loads(output)
    return Status(
        status=status_data.get("status", "unauthenticated"),
        server_url=status_data.get("serverUrl", ""),
    )


def login(email: str, password: str) -> None:
    run_command(
        [
            "bw",
            "login",
            email,
            password,
            "--raw",
        ],
    )


def logout() -> None:
    run_command(["bw", "logout"])


def set_server_url(url: str) -> None:
    run_command(["bw", "config", "server", url])


def get_session(password: str) -> str:
    os.environ.setdefault("BW_PASSWORD", password)
    return run_command(["bw", "unlock", "--raw", "--passwordenv", "BW_PASSWORD"])


def create_item(session: str, encoded_json: str) -> dict:
    output = run_command(["bw", "create", "item", encoded_json, "--session", session])
    return json.loads(output)


def create_folder(session: str, encoded_json: str) -> dict:
    output = run_command(["bw", "create", "folder", encoded_json, "--session", session])
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


def get_password(session: str, item_name: str) -> str:
    return run_command(["bw", "get", "password", item_name, "--session", session])


def get_item(session: str, id_or_name: str) -> dict:
    output = run_command(["bw", "get", "item", id_or_name, "--session", session])
    return json.loads(output)


def get_username(session: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "username", id_or_name, "--session", session])


def get_notes(session: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "notes", id_or_name, "--session", session])


def get_uri(session: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "uri", id_or_name, "--session", session])


def get_totp(session: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "totp", id_or_name, "--session", session])


def list_items(
    session: str,
    search: str | None = None,
    folder_id: str | None = None,
    collection_id: str | None = None,
    organization_id: str | None = None,
    url: str | None = None,
    trash: bool = False,
) -> list[dict]:
    cmd = ["bw", "list", "items", "--session", session]
    if search:
        cmd += ["--search", search]
    if folder_id:
        cmd += ["--folderid", folder_id]
    if collection_id:
        cmd += ["--collectionid", collection_id]
    if organization_id:
        cmd += ["--organizationid", organization_id]
    if url:
        cmd += ["--url", url]
    if trash:
        cmd.append("--trash")
    return json.loads(run_command(cmd))


def list_folders(session: str, search: str | None = None) -> list[dict]:
    cmd = ["bw", "list", "folders", "--session", session]
    if search:
        cmd += ["--search", search]
    return json.loads(run_command(cmd))


def list_collections(
    session: str,
    organization_id: str | None = None,
    search: str | None = None,
) -> list[dict]:
    cmd = ["bw", "list", "collections", "--session", session]
    if organization_id:
        cmd += ["--organizationid", organization_id]
    if search:
        cmd += ["--search", search]
    return json.loads(run_command(cmd))


def list_organizations(session: str, search: str | None = None) -> list[dict]:
    cmd = ["bw", "list", "organizations", "--session", session]
    if search:
        cmd += ["--search", search]
    return json.loads(run_command(cmd))


def edit_password(session: str, item_name: str, new_password: str) -> None:
    item = json.loads(
        run_command(["bw", "get", "item", item_name, "--session", session])
    )

    if not item.get("login"):
        raise RuntimeError(f"Item '{item_name}' is not a login item")

    item["login"]["password"] = new_password

    encoded_item = base64.b64encode(
        json.dumps(item, separators=(",", ":")).encode()
    ).decode()

    run_command(
        [
            "bw",
            "edit",
            "item",
            item["id"],
            encoded_item,
            "--session",
            session,
        ]
    )


def edit_item(session: str, item_id: str, encoded_json: str) -> dict:
    output = run_command(
        ["bw", "edit", "item", item_id, encoded_json, "--session", session]
    )
    return json.loads(output)


def edit_folder(session: str, folder_id: str, encoded_json: str) -> dict:
    output = run_command(
        ["bw", "edit", "folder", folder_id, encoded_json, "--session", session]
    )
    return json.loads(output)


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
