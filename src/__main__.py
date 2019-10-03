# import os
import sys
from pathlib import Path
sys.path.append(Path("../"))
import config

if __name__ == "__main__":
    # Yup the file is definitely main
    print(config.VERSION)
    # print(os.listdir('.'))