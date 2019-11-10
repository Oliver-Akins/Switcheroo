import os
from config import Config
from pathlib import Path
from renaming import RENAME


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
# new_filepath = {config.TARGET}/game_name/filename_from_RENAME_FILE.<ext>
def MOVE_FILE(from_filepath):
    config = Config()
    new_path = ""

    if(config.KEEP_ON_SD):
        new_path = Path(config.SOURCE, "Album", "Organized")
    else:
        pass
        # TODO Move to path other than on sd





if __name__ == "__main__":
    from_filepath = "/home/tyler/Desktop/coding/Nintendo-Switch-Photo-Manager/Nintendo/Album/2017/03/03/2017030311400900-F1C11A22FAEE3B82F21B330E1B786A39.jpg"
    MOVE_FILE(from_filepath)