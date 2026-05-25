from .command_runner import run_command


class Bitwarden:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        password: str,
        server_url: str = "https://vault.bitwarden.eu",
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._password = password
        self._server_url = server_url

    def login(self) -> None:
        run_command(
            [
                "bw",
                "login",
                self._client_id,
                self._client_secret,
                "--raw",
            ],
        )


if __name__ == "__main__":
    from pathlib import Path

    from dotenv import load_dotenv

    config = load_dotenv(
        Path(__file__).parent.parent.parent / "secrets" / "bitwarden.env"
    )

    bitwarden = Bitwarden(
        client_id=config.get("BW_CLIENT_ID"),  # type: ignore
        client_secret=config.get("BW_CLIENT_SECRET"),  # type: ignore
        password=config.get("BW_PASSWORD"),  # type: ignore
        server_url=config.get("BW_SERVER_URL"),  # type: ignore
    )

    bitwarden.login()
