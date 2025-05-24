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


def random_nums(count, limit):
    list = []
    count = limit if count > limit else count
    for i in range(count):
        num = random.randrange(0, limit)
        while num in list:
            print("redo!")
            num = random.randrange(0, limit)
        list.append(num)
    return list


def create_image_file_list(path, files=[]):
    dir_content = filter_dirs_with_period(list(path.glob("*")))
    new_files_list = files + list(filter(lambda x: x.is_file() is True, dir_content))
    for file in dir_content:
        if file.is_dir() is True:
            new_files_list = new_files_list + create_image_file_list(
                file, new_files_list
            )
        continue
    return new_files_list
