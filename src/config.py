import sys
import yaml
from pathlib import Path


_NO_ALBUM_FOLDER = """Cannot find the Album folder.\nTake some screenshots before
running the program or make sure your SOURCE_FILEPATH is correct in the config.
yaml file.\n\n"""


class Config():
    # Do not initialize the class, as we want the config attributes to be
    # constants shared throughout the various classes as we shouldn't need to
    # be modifying them at all.


    with open("config.yaml", "r") as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)

    VERSION = data["VERSION"]
    KEEP_ON_SD = data["KEEP_ON_SD_CARD"]
    FORMAT = data["FILENAME_FORMAT"]
    TARGET = data["TARGET_FILEPATH"]
    UPDATE_TITLE_IDS = data["UPDATE_TITLE_IDS"]



    SOURCE = data["SOURCE_FILEPATH"]

    # NOTE: Ensure that the album folder exists
    if not SOURCE.endswith(("/Album", "/Album/")):
        print(0)
        __dir = Path(SOURCE+"/Album")
        sys.exit(_NO_ALBUM_FOLDER)

    else:
        print(1)
        if SOURCE.endswith("Album"):
            print(2)
            SOURCE = SOURCE[:-len("Album")]
        else:
            print(3)
            SOURCE = SOURCE[:-len("Album/")]

    # NOTE: Ensure that the path indicates the inner directory
    if not SOURCE.endswith("/"): SOURCE + "/"