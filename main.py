import shelve
import os
from pathlib import Path
from helper_functions import *


def main():
    shelf = shelve.open("mydata")
    home_dir = Path.home()
    home_dir_list = filter_directories_with_period(os.listdir(home_dir))
    list_of_directories_in_home = "list of Directories:\n\n"
    ref_photo_dir = None

    for i in range(len(home_dir_list)):
        if not (home_dir_list[i].startswith(".")):
            list_of_directories_in_home += f"{i + 1}.) {home_dir_list[i]}\n"
    ref_photo_dir = input(
        (
            f"{list_of_directories_in_home}Please type in the directory name "
            "that contains the reference image files: "
        )
    )
    shelf["ref_photo_dir"] = ref_photo_dir
    print(f"shelf file :  {shelf["ref_photo_dir"]}")
    shelf.close()

    if ref_photo_dir in home_dir_list:
        print(ref_photo_dir)
    else:
        os.makedirs(f"{home_dir}/{ref_photo_dir}")


if __name__ == "__main__":
    main()
