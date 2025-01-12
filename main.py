import os


def main():
    home_dir = os.environ["HOME"]
    home_dir_list = os.listdir(home_dir)
    for directory in home_dir_list:
        if directory == "Art":
            print(os.listdir(f"{home_dir}/{'Art'}"))


main()
