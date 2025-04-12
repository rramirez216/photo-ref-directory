import os


def main():
    home_dir = os.environ["HOME"]
    home_dir_list = os.listdir(home_dir)
    list_of_directories_in_home = []
    ref_photo_dir = None
    for directory in home_dir_list:
        list_of_directories_in_home.append(directory)
    ref_photo_dir = input(
        f"{list_of_directories_in_home}type in the directory name that contains the reference image files."
    )
    print(ref_photo_dir)
    # if directory == "Art":
    #     # print(os.listdir(f"{home_dir}/{'Art'}"))
    #     ref_photo_dir = os.listdir(f"{home_dir}/{'Art'}")
    # for directory in ref_photo_dir:
    #     list = []
    #     if directory == "reference photos":
    #         currentDir = os.listdir(f"{home_dir}/Art/{directory}")
    #         for file in currentDir:
    #             list.append(currentDir)
    #     print(list)


if __name__ == "__main__":
    main()
