def filter_directories_with_period(arr, path):
    newArr = []
    for item in arr:
        item_path = path / item
        if not (item.startswith(".") or item.startswith("~") or item_path.is_file()):
            newArr.append(item)
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
