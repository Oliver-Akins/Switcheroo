import os
import sys
import json
from pathlib import Path

import gui
import decrypt
import transfer as move_utils
from renaming import rename
from config import Config

sys.path.append(Path("../"))


PROGRAM_START_MESSAGE = """

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
    https://github.com/Tyler-A/Switcheroo/issues/new
"""


def main():
    config = Config()
    # print(PROGRAM_START_MESSAGE.format(c=config))
    if config.UPDATE_TITLES:
        decrypt.update_titleids_file()

    # Iterate through ever file we can
    for file in move_utils.get_files():
        print(file)

        # Collect each part of the file needed
        filename = rename(file.parts[-1])
        filepath = file.parent


        title_id = file.parts[-1].split(".")[0].split("-")[1]



        # NOTE: Get the game name
        try:
            raise KeyError
            game_name = decrypt.get_titleid_dict()[title_id]

        except KeyError:
            if config.PROMPT_FOR_UNKNOWN:
                game_name = gui.get_unknown_game_name(file)
                print(game_name)
                # game_name = input("Unknown game name, input a filename for opened image: ")
            else:
                pass

        pass

        # TODO: Confirm the file hasn't already been moved
        if Path(move_utils.get_target_path(), filename).exists:
            continue


        # TODO: Move the file here
        # move_utils.move_file(filepath, game_name, filename)

if __name__ == "__main__":
    main()