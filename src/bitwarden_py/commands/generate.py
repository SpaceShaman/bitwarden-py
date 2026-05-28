from .command_runner import run_command


def generate_password(
    length: int = 14,
    lowercase: bool = True,
    uppercase: bool = True,
    number: bool = True,
    special: bool = True,
) -> str:
    cmd = ["bw", "generate", "--length", str(length)]
    if lowercase:
        cmd.append("--lowercase")
    if uppercase:
        cmd.append("--uppercase")
    if number:
        cmd.append("--number")
    if special:
        cmd.append("--special")
    return run_command(cmd)
