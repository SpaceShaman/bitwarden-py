import json

from .command_runner import run_command


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
