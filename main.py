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
        if directory == "reference photos":
            print(
                os.listdir(
                    f"{home_dir}/Art/reference photos/Ultimate Female Poses Sample Pack"
                )
            )


main()
