from .commands import (
    get_password,
    get_session,
    get_status,
    login,
    logout,
    set_password,
    set_server_url,
)


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
        self._session = None
        self._setup()

    def _setup(self) -> None:
        status = get_status()
        if status.status != "unauthenticated":
            logout()
        if status.server_url != self._server_url:
            set_server_url(self._server_url)
        status = get_status()
        login(self._email, self._password)
        self._session = get_session(self._password)

    def get_password(self, item_name: str) -> str:
        if not self._session:
            raise RuntimeError("Bitwarden session is not established.")
        return get_password(self._session, item_name)

    def set_password(self, item_name: str, new_password: str) -> None:
        if not self._session:
            raise RuntimeError("Bitwarden session is not established.")
        set_password(self._session, item_name, new_password)
