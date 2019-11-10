import sys
import os
from config import Config
import json
from pathlib import Path

import transfer as moveUtils
sys.path.append(Path("../"))


program_start_message = """

   _________    _________
  /         |  |         \\
 /          |  |          \\
|    ___    |  |           |
|   /   \   |  |           |
|   \___/   |  |           |
|           |  |           |
|           |  |    ___    |
|           |  |   /   \   |
|           |  |   \___/   |
|           |  |           |
|           |  |           |
|           |  |           |
 \          |  |          /
  \_________|  |_________/

Welcome to Nintendo Switch Photo Manager (V{c.VERSION})
Written by: Tyler-A and Dmynerd78

A command line utility to sort and store captures from a Nintendo Switch console.


For help on how to use it, open an issue from the link below and we can help you
from there:
    https://github.com/Tyler-A/Nintendo-Switch-Photo-Manager/issues/new
"""



if __name__ == "__main__":
    config = Config()
    #print(program_start_message.format(c=config))
    #for file in moveUtils.get_files():
    #    print(file)