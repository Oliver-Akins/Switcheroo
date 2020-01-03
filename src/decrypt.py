import os
import yaml
import urllib3
import hashlib
import xmltodict
from Crypto.Cipher import AES
from Crypto.Util import Padding

KEYHASH = "24e0dc62a15c11d38b622162ea2b4383"


def _decrypt_title_ID(key, titleid):
    """
    Converts a game titleid to the id screenshots use

    Args:
        key: Decryption key used in conversion
        titleid: titleid to convert

    Returns:
        Converted titleid
    """
    cipher = AES.new(key, AES.MODE_ECB)

    titleidb = bytes.fromhex(titleid)
    titleidb = titleidb[7::-1]
    conversion = titleidb.hex()
    conversion = conversion.ljust(32, '0')
    titleidb = bytes.fromhex(conversion)
    encrypted = cipher.encrypt(titleidb)
    screenshotid = encrypted.hex().upper()

    return screenshotid


def _load_key(filename, keyhash):
    """
    Read in key from file

    Args:
         filename: file to open
         keyhash: keyhash of the key (to ensure the key is valid)

    Returns:
        Decryption key

    Raises:
        IOError: When python has issues opening/reading the file
        ValueError: If keyhash doesn't match the hash of the computed key
    """
    with open(filename, 'r') as keyfile:
        keystring = keyfile.read(32)
        key = bytes.fromhex(keystring)

        if(hashlib.md5(key).hexdigest() not in keyhash):
            raise ValueError("Keys don't match!")

        return key


def _dl_screenshot_ids():
    """
        Generates a dictionary where each screenshot id points to the game's name
        Information obtained via nswdb.com

        Args:
            key: a key read from _load_key()

        Returns:
            Dictionary where each key is a screenshot id and it's corresponding value is the game's name

        Raises:
            ValueError: Unable to parse nswdb's titleid list
    """
    try:
        key = _load_key("key.txt", KEYHASH)
    except FileNotFoundError:
        print("Decryption key (key.txt) not found!")
        print("Unable to update games.yaml")
        return {}
    except ValueError:
        print("Decryption key (key.txt) doesn't match!")
        print("Unable to update games.yaml")
        return {}

    http = urllib3.PoolManager()
    url = "http://nswdb.com/xml.php"
    response = http.request('GET', url)

    try:
        data = xmltodict.parse(response.data)
    except:
        raise ValueError("Unable to parse titleids file")
        return

    screenshotids = {}
    dict_games = data["releases"]["release"]
    for index in range(len(dict_games)):
        curr_game = dict_games[index]

        try:
            dict_key = _decrypt_title_ID(key, curr_game["titleid"])
        except ValueError:
            # Can't decrypt key - ignore
            continue

        screenshotids[dict_key] = curr_game["name"]

    return screenshotids


def get_titleid_dict():
    """
    Reads in the cached games yaml file and loads all the items into a dictionary
    Returns an empty dictionary if it can't find the file. If games.yaml contains
    the *only* the line "F1C11A22FAEE3B82F21B330E1B786A39: Breath of the Wild" the dictionary
    will be the following: {"F1C11A22FAEE3B82F21B330E1B786A39": "Breath of the Wild"}

    Returns:
        Dictionary where each key is a screenshot id and it's corresponding value is the game's name
    """
    if not os.path.exists("games.yaml"):
        return {}

    with open("games.yaml", "r") as file:
        titleids = yaml.load(file, Loader=yaml.SafeLoader)
        return titleids


def update_titleids_file():
    """
    Updates games.yaml with new titles from __dl_screenshot_ids()
    Note: previous game names are preserved.

    Returns:
        None (Updates games.yaml file)
    """
    old_titleids = get_titleid_dict()
    new_titleids = _dl_screenshot_ids()

    new_titleids.update(old_titleids)

    with open("games.yaml", "w") as file:
        yaml.dump(new_titleids, file, width=float("inf"),
                  Dumper=yaml.SafeDumper)
