def filter_directories_with_period(arr):
    newArr = []
    for item in arr:
        if not (item.startswith(".") or item.startswith("~")):
            newArr.append(item)
    return newArr


def create_directory_list():
    return
