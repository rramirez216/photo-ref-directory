import shelve


def main():
    shelf = shelve.open("mydata")
    print(shelf["ref_photo_dir"])
    shelf.close()


if __name__ == "__main__":
    main()
