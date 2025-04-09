import os


def main():
    home_dir = os.environ["HOME"]
    home_dir_list = os.listdir(home_dir)
    ref_photo_dir = None
    for directory in home_dir_list:
        if directory == "Art":
            # print(os.listdir(f"{home_dir}/{'Art'}"))
            ref_photo_dir = os.listdir(f"{home_dir}/{'Art'}")
    for directory in ref_photo_dir:
        list = []
        if directory == "reference photos":
            currentDir = os.listdir(f"{home_dir}/Art/{directory}")
            for file in currentDir:
                list.append(currentDir)
        print(list)


if __name__ == "__main__":
    main()
