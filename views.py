from presenter import (add_entry, create_entry,
                       read_all_entries, clear_entries)


def main():
    """Головне меню програми"""
    while True:
        print("Меню:")
        print("1. Додати запис")
        print("2. Прочитати всі записи")
        print("3. Очистити список записів")
        print("4. Вийти")
        choice = input("Оберіть опцію: ")
        if choice == "1":
            add_entry(create_entry())
        elif choice == "2":
            read_all_entries()
        elif choice == "3":
            clear_entries()
        elif choice == "4":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
    