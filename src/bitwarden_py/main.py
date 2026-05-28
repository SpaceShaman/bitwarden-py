from typing import Any

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
    generate_password,
    get_item,
    get_notes,
    get_password,
    get_status,
    get_template,
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
    sync,
)


class Bitwarden:
    def __init__(
        self,
        email: str,
        password: str,
        server_url: str = "https://vault.bitwarden.eu",
    ):
        self._password = password
        status = get_status()
        if status.user_email != email and status.status != "unauthenticated":
            logout()
            status.status = "unauthenticated"
        if status.server_url != server_url:
            if status.status != "unauthenticated":
                logout()
                status.status = "unauthenticated"
            set_server_url(server_url)
        if status.status == "unauthenticated":
            login(email, password)
        sync()

    def logout(self) -> None:
        logout()

    def sync(self) -> None:
        sync()

    def create_item(self, item: dict[str, Any]) -> dict[str, Any]:
        return create_item(self._password, item)

    def create_folder(self, folder: dict[str, Any]) -> dict[str, Any]:
        return create_folder(self._password, folder)

    def create_attachment(self, file_path: str, item_id: str) -> dict[str, Any]:
        return create_attachment(self._password, file_path, item_id)

    def get_password(self, item_name: str) -> str:
        return get_password(self._password, item_name)

    def get_item(self, id_or_name: str) -> dict[str, Any]:
        return get_item(self._password, id_or_name)

    def get_username(self, id_or_name: str) -> str:
        return get_username(self._password, id_or_name)

    def get_notes(self, id_or_name: str) -> str:
        return get_notes(self._password, id_or_name)

    def get_uri(self, id_or_name: str) -> str:
        return get_uri(self._password, id_or_name)

    def get_totp(self, id_or_name: str) -> str:
        return get_totp(self._password, id_or_name)

    def get_template(self, object_type: str) -> dict[str, Any]:
        return get_template(object_type)

    def list_items(
        self,
        search: str | None = None,
        folder_id: str | None = None,
        collection_id: str | None = None,
        organization_id: str | None = None,
        url: str | None = None,
        trash: bool = False,
    ) -> list[dict[str, Any]]:
        return list_items(
            self._password,
            search=search,
            folder_id=folder_id,
            collection_id=collection_id,
            organization_id=organization_id,
            url=url,
            trash=trash,
        )

    def list_folders(self, search: str | None = None) -> list[dict[str, Any]]:
        return list_folders(self._password, search=search)

    def list_collections(
        self,
        organization_id: str | None = None,
        search: str | None = None,
    ) -> list[dict[str, Any]]:
        return list_collections(
            self._password, organization_id=organization_id, search=search
        )

    def list_organizations(self, search: str | None = None) -> list[dict[str, Any]]:
        return list_organizations(self._password, search=search)

    def edit_password(self, item_name: str, new_password: str) -> None:
        edit_password(self._password, item_name, new_password)

    def edit_item(self, item_id: str, item: dict[str, Any]) -> dict[str, Any]:
        return edit_item(self._password, item_id, item)

    def edit_folder(self, folder_id: str, folder: dict[str, Any]) -> dict[str, Any]:
        return edit_folder(self._password, folder_id, folder)

    def delete_item(self, item_id: str, permanent: bool = False) -> None:
        delete_item(self._password, item_id, permanent=permanent)

    def delete_folder(self, folder_id: str, permanent: bool = False) -> None:
        delete_folder(self._password, folder_id, permanent=permanent)

    def delete_attachment(self, attachment_id: str, item_id: str) -> None:
        delete_attachment(self._password, attachment_id, item_id)

    def generate_password(
        self,
        length: int = 14,
        lowercase: bool = True,
        uppercase: bool = True,
        number: bool = True,
        special: bool = True,
    ) -> str:
        return generate_password(
            length,
            lowercase,
            uppercase,
            number,
            special,
        )
