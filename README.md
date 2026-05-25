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

### `Bitwarden(email, password, server_url?)`

Creates a new client and authenticates with the vault.

| Parameter    | Type  | Default                          | Description                        |
|--------------|-------|----------------------------------|------------------------------------|
| `email`      | `str` | —                                | Your Bitwarden account email       |
| `password`   | `str` | —                                | Your master password               |
| `server_url` | `str` | `"https://vault.bitwarden.eu"`   | Bitwarden server URL               |

### `bw.get_password(item_name) → str`

Returns the password of the vault item matching `item_name`.

### `bw.set_password(item_name, new_password) → None`

Updates the password of the vault item matching `item_name`.

---

## License

[MIT](LICENSE)
