import sys
from Config import Config
from pathlib import Path

import transfer as moveUtils
sys.path.append(Path("../"))

if __name__ == "__main__":
    config = Config()
    print(config.SOURCE[:-len("Album")])
    print(config.VERSION)
    moveUtils.GET_FILES_TO_MOVE()