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

    # CONSTANTS
    VERSION = "0.1.0"
    VIDEO_FORMATS = ["mp4", "mkv"]
    IMAGE_FORMATS = ["png", "jpg", "jpeg"]


    # USER ASSIGNED VARIABLES
    KEEP_ON_SD = data["KEEP_ON_SD_CARD"]
    FORMAT = data["FILENAME_FORMAT"]
    TARGET = data["TARGET_FILEPATH"]
    UPDATE_TITLES = data["UPDATE_TITLE_IDS"]
    SOURCE = data["SOURCE_FILEPATH"]
    DO_IMAGES = data["INCLUDE_IMAGES"]
    DO_VIDEOS = data["INCLUDE_VIDEOS"]
    PROMPT_FOR_UNKNOWN = data["PROMPT_FOR_UNKNOWN"]


    # NOTE: Ensure that the album folder exists
    if not SOURCE.endswith(("/Album", "/Album/")):
        __dir = Path(SOURCE+"/Album")
        sys.exit(_NO_ALBUM_FOLDER)

    else:
        if SOURCE.endswith("Album"):
            SOURCE = SOURCE[:-len("Album")]
        else:
            SOURCE = SOURCE[:-len("Album/")]


    # NOTE: Ensure that the path indicates the inner directory
    if not SOURCE.endswith("/"): SOURCE + "/"


    # NOTE: Ensure we have something to do
    if (not DO_IMAGES) and (not DO_VIDEOS):
        sys.exit("You must specify one type of file to manage in your config.")