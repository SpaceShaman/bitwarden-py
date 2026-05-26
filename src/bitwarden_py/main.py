import base64
import json

from .commands import (
    create_attachment,
    create_folder,
    create_item,
    delete_attachment,
    delete_folder,
    delete_item,
    edit_folder,
    edit_item,
    edit_password,
    get_item,
    get_notes,
    get_password,
    get_session,
    get_status,
    get_totp,
    get_uri,
    get_username,
    list_collections,
    list_folders,
    list_items,
    list_organizations,
    login,
    logout,
    set_server_url,
)


class Bitwarden:
    def __init__(
        self,
        email: str,
        password: str,
        server_url: str = "https://vault.bitwarden.eu",
    ):
        status = get_status()
        if status.status != "unauthenticated":
            logout()
        if status.server_url != server_url:
            set_server_url(server_url)
        login(email, password)
        self._session = get_session(password)

    @staticmethod
    def _encode(data: dict) -> str:
        return base64.b64encode(
            json.dumps(data, separators=(",", ":")).encode()
        ).decode()

    def create_item(self, item: dict) -> dict:
        return create_item(self._session, self._encode(item))

    def create_folder(self, folder: dict) -> dict:
        return create_folder(self._session, self._encode(folder))

    def create_attachment(self, file_path: str, item_id: str) -> dict:
        return create_attachment(self._session, file_path, item_id)

    def get_password(self, item_name: str) -> str:
        return get_password(self._session, item_name)

    def get_item(self, id_or_name: str) -> dict:
        return get_item(self._session, id_or_name)

    def get_username(self, id_or_name: str) -> str:
        return get_username(self._session, id_or_name)

    def get_notes(self, id_or_name: str) -> str:
        return get_notes(self._session, id_or_name)

    def get_uri(self, id_or_name: str) -> str:
        return get_uri(self._session, id_or_name)

    def get_totp(self, id_or_name: str) -> str:
        return get_totp(self._session, id_or_name)

    def list_items(
        self,
        search: str | None = None,
        folder_id: str | None = None,
        collection_id: str | None = None,
        organization_id: str | None = None,
        url: str | None = None,
        trash: bool = False,
    ) -> list[dict]:
        return list_items(
            self._session,
            search=search,
            folder_id=folder_id,
            collection_id=collection_id,
            organization_id=organization_id,
            url=url,
            trash=trash,
        )

    def list_folders(self, search: str | None = None) -> list[dict]:
        return list_folders(self._session, search=search)

    def list_collections(
        self,
        organization_id: str | None = None,
        search: str | None = None,
    ) -> list[dict]:
        return list_collections(
            self._session, organization_id=organization_id, search=search
        )

    def list_organizations(self, search: str | None = None) -> list[dict]:
        return list_organizations(self._session, search=search)

    def edit_password(self, item_name: str, new_password: str) -> None:
        edit_password(self._session, item_name, new_password)

    def edit_item(self, item_id: str, item: dict) -> dict:
        return edit_item(self._session, item_id, self._encode(item))

    def edit_folder(self, folder_id: str, folder: dict) -> dict:
        return edit_folder(self._session, folder_id, self._encode(folder))

    def delete_item(self, item_id: str, permanent: bool = False) -> None:
        delete_item(self._session, item_id, permanent=permanent)

    def delete_folder(self, folder_id: str, permanent: bool = False) -> None:
        delete_folder(self._session, folder_id, permanent=permanent)

    def delete_attachment(self, attachment_id: str, item_id: str) -> None:
        delete_attachment(self._session, attachment_id, item_id)
