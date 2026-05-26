# bitwarden-py

> A simple Python wrapper for the [Bitwarden CLI](https://bitwarden.com/help/cli/) — programmatically read and update passwords stored in your Bitwarden vault.

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bitwarden-py)](https://pypi.org/project/bitwarden-py)
[![PyPI - Version](https://img.shields.io/pypi/v/bitwarden-py)](https://pypi.org/project/bitwarden-py)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/badge/linting-Ruff-black?logo=ruff&logoColor=black)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![GitHub License](https://img.shields.io/github/license/SpaceShaman/bitwarden-py)](https://github.com/SpaceShaman/bitwarden-py?tab=MIT-1-ov-file)

---

## Requirements

### Bitwarden CLI

`bitwarden-py` calls the official `bw` binary under the hood, so you must have it installed and available in your `PATH`.

Install it by following the official guide:  
👉 [https://bitwarden.com/help/cli/#download-and-install](https://bitwarden.com/help/cli/#download-and-install)

Quick install options:

```bash
# macOS (Homebrew)
brew install bitwarden-cli

# Windows (Chocolatey)
choco install bitwarden-cli

# npm (cross-platform)
npm install -g @bitwarden/cli
```

After installation, verify it works:

```bash
bw --version
```

---

## Installation

```bash
pip install bitwarden-py
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add bitwarden-py
```

---

## Quick Start

```python
from bitwarden_py import Bitwarden

bw = Bitwarden(
    email="your@email.com",
    password="your_master_password",
)

# Fetch a password by item name
db_password = bw.get_password("My Database")
print(db_password)  # → "s3cr3t!"

# Update the password of an item
bw.set_password("My Database", "n3wp4ssw0rd")
```

### Using a self-hosted server

By default the library points to `https://vault.bitwarden.eu`.  
Pass `server_url` to connect to a different instance:

```python
bw = Bitwarden(
    email="your@email.com",
    password="your_master_password",
    server_url="https://bitwarden.yourcompany.com",
)
```

---

## API Reference

> For the full Bitwarden CLI documentation, see 👉 [https://bitwarden.com/help/cli/](https://bitwarden.com/help/cli/)

### `Bitwarden(email, password, server_url?)`

Creates a new client and authenticates with the vault.

| Parameter    | Type  | Default                          | Description                        |
|--------------|-------|----------------------------------|------------------------------------|
| `email`      | `str` | —                                | Your Bitwarden account email       |
| `password`   | `str` | —                                | Your master password               |
| `server_url` | `str` | `"https://vault.bitwarden.eu"`   | Bitwarden server URL               |

---

### Create

#### `bw.create_item(item) → dict`

Creates a new vault item. Use `bw.get_template("item")` to obtain the base structure.

```python
template = bw.get_template("item")
template["name"] = "My Login"
template["login"]["username"] = "user@example.com"
template["login"]["password"] = "s3cr3t"
new_item = bw.create_item(template)
```

#### `bw.create_folder(folder) → dict`

Creates a new folder. Use `bw.get_template("folder")` to obtain the base structure.

```python
template = bw.get_template("folder")
template["name"] = "Work"
new_folder = bw.create_folder(template)
```

#### `bw.create_attachment(file_path, item_id) → dict`

Attaches a file to an existing vault item.

```python
bw.create_attachment("./secret.txt", "16b15b89-65b3-4639-ad2a-95052a6d8f66")
```

---

### Read

#### `bw.get_password(item_name) → str`

Returns the password of the vault item matching `item_name`.

#### `bw.get_item(id_or_name) → dict`

Returns the full vault item object matching the given ID or name.

#### `bw.get_username(id_or_name) → str`

Returns the username of the vault item matching the given ID or name.

#### `bw.get_notes(id_or_name) → str`

Returns the notes of the vault item matching the given ID or name.

#### `bw.get_uri(id_or_name) → str`

Returns the URI of the vault item matching the given ID or name.

#### `bw.get_totp(id_or_name) → str`

Returns the current TOTP code for the vault item matching the given ID or name.

#### `bw.get_template(object_type) → dict`

Returns the JSON template for the given object type. Useful for constructing objects to pass to `create_*` and `edit_*` methods.

Supported types: `item`, `item.field`, `item.login`, `item.login.uri`, `item.card`, `item.identity`, `item.securenote`, `folder`, `collection`, `item-collections`, `org-collection`.

#### `bw.list_items(search?, folder_id?, collection_id?, organization_id?, url?, trash?) → list[dict]`

Returns a list of vault items. All parameters are optional and act as filters.

| Parameter         | Type   | Description                              |
|-------------------|--------|------------------------------------------|
| `search`          | `str`  | Filter by search term                    |
| `folder_id`       | `str`  | Filter by folder ID (`null` / `notnull`) |
| `collection_id`   | `str`  | Filter by collection ID                  |
| `organization_id` | `str`  | Filter by organization ID                |
| `url`             | `str`  | Filter by URI                            |
| `trash`           | `bool` | If `True`, list items in the trash       |

#### `bw.list_folders(search?) → list[dict]`

Returns a list of folders, optionally filtered by `search`.

#### `bw.list_collections(organization_id?, search?) → list[dict]`

Returns a list of collections, optionally filtered by organization ID or search term.

#### `bw.list_organizations(search?) → list[dict]`

Returns a list of organizations, optionally filtered by `search`.

---

### Edit

#### `bw.edit_password(item_name, new_password) → None`

Updates the password of the vault item matching `item_name`.

#### `bw.edit_item(item_id, item) → dict`

Replaces a vault item with the provided dict. Fetch the current item with `get_item` first, modify it, then pass it here.

```python
item = bw.get_item("7ac9cae8-5067-4faf-b6ab-acfd00e2c328")
item["login"]["password"] = "newp@ssw0rd"
bw.edit_item(item["id"], item)
```

#### `bw.edit_folder(folder_id, folder) → dict`

Replaces a folder with the provided dict.

---

### Delete

#### `bw.delete_item(item_id, permanent?) → None`

Sends an item to the trash. Pass `permanent=True` to delete it immediately without going through trash.

#### `bw.delete_folder(folder_id, permanent?) → None`

Deletes a folder. Pass `permanent=True` to skip trash.

#### `bw.delete_attachment(attachment_id, item_id) → None`

Deletes an attachment from a vault item.

---

## License

[MIT](LICENSE)
