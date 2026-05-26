import json

from .command_runner import run_command


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
