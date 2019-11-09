import os
from config import Config
from pathlib import Path


def GET_FILES_TO_MOVE():
    """
        Generates files that have not been moved yet. Each yield is a full file path
    """
    config = Config()
    files = Path(config.SOURCE + "Album/").glob
    print(files)



"""
GET LIST OF FILES (TYLKER)
RENAME ALL FILES IN THE LIST (RENAME_FILE (only accepts the filename, not full path))
"""

def MOVE_FILE(from_filepath, to_filepath):
    config = Config()


if __name__ == "__main__":
    GET_FILES_TO_MOVE()