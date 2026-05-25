from .commands import get_status, login, logout, set_server_url


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
        status = get_status()
        if status.server_url != self._server_url:
            if status.status != "unauthenticated":
                logout()
            set_server_url(self._server_url)
        status = get_status()
        if status.status == "unauthenticated":
            login(self._email, self._password)
