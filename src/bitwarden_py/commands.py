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


def get_password(session: str, item_name: str) -> str:
    return run_command(["bw", "get", "password", item_name, "--session", session])


def set_password(session: str, item_name: str, new_password: str) -> None:
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
