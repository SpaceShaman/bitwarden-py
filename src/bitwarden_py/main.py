import json
from dataclasses import dataclass
from typing import Literal

from .command_runner import run_command


@dataclass
class Status:
    status: Literal["locked", "unlocked", "unauthenticated"]
    server_url: str


class Bitwarden:
    def __init__(
        self,
        email: str,
        password: str,
        server_url: str = "https://vault.bitwarden.eu",
    ):
        self._email = email
        self._password = password
        self._server_url = server_url
        self._setup()

    def _setup(self) -> None:
        status = self._get_status()
        if status.server_url != self._server_url:
            if status.status != "unauthenticated":
                self._logout()
            self._set_server_url()
        status = self._get_status()
        if status.status == "unauthenticated":
            self._login()

    def _get_status(self) -> Status:
        output = run_command(["bw", "status"])
        status_data = json.loads(output)
        return Status(
            status=status_data.get("status", "unauthenticated"),
            server_url=status_data.get("serverUrl", ""),
        )

    def _login(self) -> None:
        run_command(
            [
                "bw",
                "login",
                self._email,
                self._password,
                "--raw",
            ],
        )

    def _logout(self) -> None:
        run_command(["bw", "logout"])

    def _set_server_url(self) -> None:
        run_command(["bw", "config", "server", self._server_url])
