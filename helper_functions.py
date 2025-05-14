import shutil
import random
from functools import reduce


def filter_dirs_with_period(arr, path=None):
    newArr = []
    for item in arr:
        if path is None:
            if not (item.name.startswith(".") or item.name.startswith("~")):
                newArr.append(item)
        else:
            item_path = path / item
            if not (
                item.startswith(".") or item.startswith("~") or item_path.is_file()
            ):
                newArr.append(item)
    return newArr


def create_directory_list(arr):
    # return "list of Directories:\n\n" + reduce(
    #     lambda accumulator, str: accumulator + str, arr
    # )
    return "list of Directories:\n\n" + "".join(arr)


def prepend_bullet_and_append_newline(item):
    return f"- {item}\n"


def create_command_list():
    return (
        "Usage:\n"
        "    ref [command]\n\n"
        "Available Commands:\n"
        "    add\n"
        "    reset\n"
        "    current\n"
        "    shuffle\n"
    )


def copy_file(source, destination):
    shutil.copy(source, destination)


def random_nums(amount, length):
    list = []
    for i in range(amount):
        num = random.randrange(0, length)
        if length > amount:
            while num in list:
                print("redo!")
                num = random.randrange(0, length)
        list.append(num)
    return list
