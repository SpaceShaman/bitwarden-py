import subprocess


def run_command(command: list[str], password: str | None = None) -> str:
    try:
        result = subprocess.run(
            command,
            input=password,
            stdin=None if password else subprocess.DEVNULL,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.stderr.strip()) from None
