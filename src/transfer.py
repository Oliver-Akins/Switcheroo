import os
from config import Config
from pathlib import Path
from renaming import rename


def get_files():
    """
        Generates files that have not been moved yet. Each yield is a full file path
    """

    config = Config()
    files = []

    # Collect all the files we need to generate
    source = Path(config.SOURCE + "Album/").glob(
        "[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]/*"
    )

    # Generate each file
    for file in source:
        file_ext = str(file).split(".")[-1]
        if config.DO_IMAGES and file_ext in config.IMAGE_FORMATS:
            yield file
        elif config.DO_VIDEOS and file_ext in config.VIDEO_FORMATS:
            yield file



# from_filepath = /.../Nintendo/Album/2019/11/9/date-titleid.png
#
# new_filepath = {config.TARGET}/game_name/filename_parameter.<ext>
def move_file(from_filepath, game_name, filename):
    config = Config()
    print(f"from_filepath: {from_filepath}\ngame_name: {game_name}\nfilename: {filename}")
    new_path = ""

    if(config.KEEP_ON_SD):
        new_path = Path(config.SOURCE, "Album", "Organized")
    else:
        pass
        # TODO Move to path other than on sd



# This should return the filepath of where we are wanting to move the file to, this will return a Path object
def get_target_path():
    return ""
