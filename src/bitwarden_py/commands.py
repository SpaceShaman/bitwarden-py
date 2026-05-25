import json
import os
import subprocess
from dataclasses import dataclass
from typing import Literal


@dataclass
class Status:
    status: Literal["locked", "unlocked", "unauthenticated"]
    server_url: str


def get_status() -> Status:
    output = _run_command(["bw", "status"])
    status_data = json.loads(output)
    return Status(
        status=status_data.get("status", "unauthenticated"),
        server_url=status_data.get("serverUrl", ""),
    )


def login(email: str, password: str) -> None:
    _run_command(
        [
            "bw",
            "login",
            email,
            password,
            "--raw",
        ],
    )


def logout() -> None:
    _run_command(["bw", "logout"])


def set_server_url(url: str) -> None:
    _run_command(["bw", "config", "server", url])


def get_session(password: str) -> str:
    os.environ.setdefault("BW_PASSWORD", password)
    return _run_command(["bw", "unlock", "--raw", "--passwordenv", "BW_PASSWORD"])


def get_password(session: str, item_name: str) -> str:
    return _run_command(["bw", "get", "password", item_name, "--session", session])


def _run_command(command: list[str]) -> str:
    try:
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            stdin=subprocess.DEVNULL,
        ).stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.stderr.strip()) from e
