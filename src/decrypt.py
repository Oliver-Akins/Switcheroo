import os
import urllib3
import hashlib
import xmltodict
from Crypto.Cipher import AES
from Crypto.Util import Padding

KEYHASH = "24e0dc62a15c11d38b622162ea2b4383"


def decrypt_title_ID(key, titleid):
    cipher = AES.new(key, AES.MODE_ECB)

    titleidb = bytes.fromhex(titleid)
    titleidb = titleidb[7::-1]
    conversion = titleidb.hex()
    conversion = conversion.ljust(32, '0')
    titleidb = bytes.fromhex(conversion)
    encrypted = cipher.encrypt(titleidb)
    screenshotid = encrypted.hex().upper()

    return screenshotid


def load_key(filename, keyhash):
    try:
        with open(filename, 'r') as keyfile:
                keystring = keyfile.read(32)
                key = bytes.fromhex(keystring)
                if(hashlib.md5(key).hexdigest() not in keyhash):
                    raise ValueError("Keys don't match!")
                return key

    except FileNotFoundError:
        print("Decryption key (key.txt) not found!")
    except ValueError:
        print("Decryption key (key.txt) doesn't match!")


def get_title_IDs(key):
    titleids = {}
    http = urllib3.PoolManager()
    url = "http://nswdb.com/xml.php"
    response = http.request('GET', url)

    try:
        data = xmltodict.parse(response.data)
    except:
        print(f"Failed to parse xml from response ({traceback.format_exc()})")
    pass

    dict_games = data["releases"]["release"]
    num_games = len(dict_games)

    for index in range(num_games):
        curr = dict_games[index]
        try:
            dict_key = decrypt_title_ID(key, curr["titleid"])
        except ValueError:
            continue  # Can't decrypt key - ignore

        titleids[dict_key] = curr["name"]

    return titleids

def update_titleid_dict():
    if not os.path.isfile("key.txt"):
        print("Unable to update titleIDs from online (key.txt does not exist)")

    key = load_key("key.txt", KEYHASH)
    ids = get_title_IDs(key)

    return ids


if __name__ == "__main__":
    id_dict = update_titleid_dict()
    print(id_dict)