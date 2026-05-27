import json
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


def sync() -> None:
    run_command(["bw", "sync"])
