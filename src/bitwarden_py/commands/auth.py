import json
from dataclasses import dataclass
from enum import Enum
from typing import Literal

from .command_runner import run_command


@dataclass
class Status:
    status: Literal["locked", "unlocked", "unauthenticated"]
    server_url: str
    user_email: str


class MFAMethod(Enum):
    TOTP = "0"
    Email = "1"
    Yubikey = "2"


def get_status() -> Status:
    output = run_command(["bw", "status"])
    status_data = json.loads(output)
    return Status(
        status=status_data.get("status", "unauthenticated"),
        server_url=status_data.get("serverUrl", ""),
        user_email=status_data.get("userEmail", ""),
    )


def login(
    email: str,
    password: str,
    mfa_method: MFAMethod | None = None,
    mfa_code: str | None = None,
) -> None:
    command = [
        "bw",
        "login",
        email,
        password,
        "--raw",
    ]
    if mfa_method and mfa_code:
        command.extend(["--method", mfa_method.value, "--code", mfa_code])

    run_command(command)


def logout() -> None:
    run_command(["bw", "logout"])


def set_server_url(url: str) -> None:
    run_command(["bw", "config", "server", url])


def sync() -> None:
    run_command(["bw", "sync"])
