import sys
from config import Config
from pathlib import Path

import transfer as moveUtils
sys.path.append(Path("../"))

if __name__ == "__main__":
    config = Config()
    print(config.VERSION)
    for file in moveUtils.get_files():
        print(file)