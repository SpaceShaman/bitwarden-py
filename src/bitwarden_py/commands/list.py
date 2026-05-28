import json
from typing import Any

from .command_runner import run_command


def list_items(
    password: str,
    search: str | None = None,
    folder_id: str | None = None,
    collection_id: str | None = None,
    organization_id: str | None = None,
    url: str | None = None,
    trash: bool = False,
) -> list[dict[str, Any]]:
    cmd = ["bw", "list", "items"]
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
    return json.loads(run_command(cmd, password=password))


def list_folders(password: str, search: str | None = None) -> list[dict[str, Any]]:
    cmd = ["bw", "list", "folders"]
    if search:
        cmd += ["--search", search]
    return json.loads(run_command(cmd, password=password))


def list_collections(
    password: str,
    organization_id: str | None = None,
    search: str | None = None,
) -> list[dict[str, Any]]:
    cmd = ["bw", "list", "collections"]
    if organization_id:
        cmd += ["--organizationid", organization_id]
    if search:
        cmd += ["--search", search]
    return json.loads(run_command(cmd, password=password))


def list_organizations(
    password: str, search: str | None = None
) -> list[dict[str, Any]]:
    cmd = ["bw", "list", "organizations"]
    if search:
        cmd += ["--search", search]
    return json.loads(run_command(cmd, password=password))
