import fcntl
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .command_runner import run_command

_SESSION_FILE = Path.home() / ".cache" / "bitwarden-py" / "session"
_LOCK_FILE = Path.home() / ".cache" / "bitwarden-py" / "session.lock"


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
    clear_session()


def set_server_url(url: str) -> None:
    run_command(["bw", "config", "server", url])


def get_session(password: str) -> str:
    _LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(_LOCK_FILE, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            if session := _read_session():
                return session
            os.environ["BW_PASSWORD"] = password
            session = run_command(
                ["bw", "unlock", "--raw", "--passwordenv", "BW_PASSWORD"]
            )
            os.environ.pop("BW_PASSWORD", None)
            _write_session(session)
            return session
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def clear_session() -> None:
    _SESSION_FILE.unlink(missing_ok=True)


def _read_session() -> str | None:
    if _SESSION_FILE.exists():
        return _SESSION_FILE.read_text() or None
    return None


def _write_session(session: str) -> None:
    _SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    _SESSION_FILE.write_text(session)
