from pathlib import Path


def path_apk(path: str):
    return Path(__file__).parent.parent.parent.joinpath(path).absolute().__str__()
