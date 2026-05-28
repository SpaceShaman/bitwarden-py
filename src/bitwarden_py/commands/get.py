import json
from typing import Any

from .command_runner import run_command


def get_password(password: str, item_name: str) -> str:
    return run_command(["bw", "get", "password", item_name], password=password)


def get_item(password: str, id_or_name: str) -> dict[str, Any]:
    output = run_command(["bw", "get", "item", id_or_name], password=password)
    return json.loads(output)


def get_username(password: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "username", id_or_name], password=password)


def get_notes(password: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "notes", id_or_name], password=password)


def get_uri(password: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "uri", id_or_name], password=password)


def get_totp(password: str, id_or_name: str) -> str:
    return run_command(["bw", "get", "totp", id_or_name], password=password)


def get_template(object_type: str) -> dict[str, Any]:
    output = run_command(["bw", "get", "template", object_type])
    return json.loads(output)
