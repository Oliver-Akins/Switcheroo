# Python modules:
# from pathlib import Path
# from os import path
# import argparse


# # Argument parsing
# parser = argparse.ArgumentParser(
#     description="Organize & Timestamp Nintendo Switch Captures"
# )

# parser.add_argument(
#     "input_filepath",
#     type=Path,
#     help="The full filepath for the 'Nintendo/Album' folder."
# )

# parser.add_argument(
#     "output_filepath",
#     type=Path,
#     help="The folder where you want re-sorted files to go."
# )

# args = parser.parse_args()



# from PIL import Image
# from time import sleep
# image_thing = Image.open('./Output/droplet.png')
# image_thing.show()
# print(1)
# sleep(10)
# print(2)
# image_thing.close()




import config
from src.renaming import *
RENAME("2019051913454200-F1C11A22FAEE3B82F21B330E1B786A39", config.FILENAME_FORMAT)