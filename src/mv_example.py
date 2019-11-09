from pathlib import Path
import shutil

def get_title_from_screenshotid():
    return "Breath of the Wild"

def rename_file(old_name):
    # TEMPORARY WILL BE REMOVED
    # 2017030311400900-F1C11A22FAEE3B82F21B330E1B786A39.jpg -> 2017-03-03-11400900.jpg
    date = old_name.split("-")[0]

    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    time = date[8:]

    return f"{year}-{day}-{month}-{time}.{old_name[-3:]}"


from_dest = Path("Nintendo", "Album", "2017", "03", "03", "2017030311400900-F1C11A22FAEE3B82F21B330E1B786A39.jpg")
output_dir = Path("Nintendo", "Album", "Organized")
output_dest = Path("Nintendo", "Album", "Organized") / get_title_from_screenshotid()

# Need to check to see if output exists to prevent other mkdirs from breaking
if not output_dir.exists():
    output_dir.mkdir()

if not output_dest.exists():
    output_dest.mkdir()

new_filepath = output_dest / rename_file(from_dest.name)

if not new_filepath.exists():
    print("Copying file")
    shutil.copyfile(from_dest, new_filepath)
