import getManga


def main_menu():
    """
    This function represent the menu of the all program
    :return: none
    """
    while True:
        print("--------NETTRUYEN DOWNLOADER Menu----------")
        print("What would you like to do?: ")
        print("1: Tải truyện từ chap lớn nhất tới chap chỉ định")
        print("Nhấp EXIT để thoát")
        print("-----\n-----")
        option = input("Your choice:  ")
        if option == "1":
            getManga.getManga()
        else:
            print("Please input 1-... options: ")


if __name__ == '__main__':
    main_menu()
