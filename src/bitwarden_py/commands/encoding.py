import base64
import json
from typing import Any


def encode(data: dict[str, Any]) -> str:
    return base64.b64encode(json.dumps(data, separators=(",", ":")).encode()).decode()
