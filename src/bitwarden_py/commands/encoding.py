import base64
import json


def encode(data: dict) -> str:
    return base64.b64encode(
        json.dumps(data, separators=(",", ":")).encode()
    ).decode()
