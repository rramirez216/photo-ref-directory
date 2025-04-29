import shutil
import random


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
    # print(newArr)
    return newArr


def create_directory_list():
    return


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
        list.append(random.randrange(0, length))
    print(list)
    return list


random_nums(4, 11)
