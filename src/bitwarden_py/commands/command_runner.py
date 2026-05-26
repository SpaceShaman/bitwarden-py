import subprocess


def run_command(command: list[str]) -> str:
    try:
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            stdin=subprocess.DEVNULL,
        ).stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.stderr.strip()) from None
