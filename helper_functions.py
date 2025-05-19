import shutil
import random


def filter_dirs_with_period(arr, path=None):
    if path is None:
        return list(
            filter(
                lambda item: not (
                    item.name.startswith(".") or item.name.startswith("~")
                ),
                arr,
            )
        )
    return list(
        filter(
            lambda item: not (
                item.startswith(".") or item.startswith("~") or (path / item).is_file()
            ),
            arr,
        )
    )


def create_directory_list(iterable):
    return "list of Directories:\n\n" + "".join(iterable)


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
