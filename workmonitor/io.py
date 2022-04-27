from pathlib import Path

SESSIONS_PATH = Path(__file__).parent.parent / "data" / "sessions.txt"


def read_sessions_data(sessions_path: Path | str = SESSIONS_PATH):
    with open(sessions_path, mode="r") as file:
        return file.read().splitlines()


def append_session(sess_str: str, sessions_path: Path | str = SESSIONS_PATH):
    with open(sessions_path, mode="a") as file:
        file.write(sess_str + "\n")
