# a script for creating the apworld
# (This is not a module for Archipelago. This is a stand-alone script.)
import os
import zlib
from shutil import copytree, rmtree, make_archive

# run from working directory cliffredux - working directory will be changed to ..

# directory "SuperJunkoidRandomizer" (with the correct version) needs to be a sibling to "Archipelago"
# This does not verify the version.

ORIG = "cliffredux"
TEMP = "cliffredux_temp"
MOVE = "cliffredux_move"

if os.getcwd().endswith("Archipelago"):
    os.chdir("worlds")
else:
    os.chdir("..")
assert os.getcwd().endswith("worlds"), f"incorrect directory: {os.getcwd()=}"

assert os.path.exists(ORIG), f"{ORIG} doesn't exist"
assert not os.path.exists(TEMP), f"{TEMP} exists"
assert not os.path.exists(MOVE), f"{MOVE} exists"

cliff_redux_randomizer_dir = os.path.join("..", "..", "CliffReduxRandomizer", "src", "cliff_redux_randomizer")
assert os.path.exists(cliff_redux_randomizer_dir), f"{cliff_redux_randomizer_dir} doesn't exist"

destination = os.path.join("cliffredux.apworld")
if os.path.exists(destination):
    os.unlink(destination)
assert not os.path.exists(destination)

copytree(ORIG, TEMP)

if os.path.exists(os.path.join(TEMP, "__pycache__")):
    rmtree(os.path.join(TEMP, "__pycache__"))

copytree(cliff_redux_randomizer_dir, os.path.join(TEMP, "cliff_redux_randomizer"))

if os.path.exists(os.path.join(TEMP, "cliff_redux_randomizer", "__pycache__")):
    rmtree(os.path.join(TEMP, "cliff_redux_randomizer", "__pycache__"))


def lib_crc() -> int:
    crc = 0
    for p, _dir_names, file_names in os.walk(os.path.join(TEMP, "cliff_redux_randomizer")):
        for file_name in file_names:
            full_path = os.path.join(p, file_name)
            with open(full_path, 'rb') as file:
                crc = zlib.crc32(file.read(), crc)
    return crc


crc = lib_crc()
print(f"writing crc {crc}")
with open(os.path.join(TEMP, "cliff_redux_randomizer", "crc"), "w") as crc_file:
    crc_file.write(f"{crc}")
with open(os.path.join(TEMP, "lib_crc.py"), "w") as crc_module:
    crc_module.write(f"crc = {crc}\n")

zip_file_name = make_archive("cliffredux", "zip", ".", TEMP)
print(f"{zip_file_name} -> {destination}")
os.rename(zip_file_name, destination)

rmtree(TEMP)

assert os.path.exists(ORIG), f"{ORIG} doesn't exist at end"
assert not os.path.exists(TEMP), f"{TEMP} exists at end"
assert not os.path.exists(MOVE), f"{MOVE} exists at end"
