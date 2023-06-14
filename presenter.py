from file_models import FILENAME
import pickle


def add_entry(entry, entries):
    """Add an entry to the list"""
    entries.append(entry)
    save_entries(entries)
    print("Запис доданий успішно!")


def create_entry():
    """Create a new entry"""
    new_entry = {}
    print("Створіть новий запис:")
    new_entry["Title"] = input("Введіть назву: ")
    new_entry["Content"] = input("Введіть текст: ")
    return new_entry


def read_entries():
    """Read all entries from the file"""
    try:
        with open(FILENAME, "rb") as file:
            entries = pickle.load(file)
    except FileNotFoundError:
        entries = []
    return entries


def save_entries(entries):
    """Save entries to the file"""
    with open(FILENAME, "wb") as file:
        pickle.dump(entries, file)


def read_all_entries(entries):
    """Display all entries"""
    if entries:
        for index, entry in enumerate(entries, 1):
            print(f"Запись #{index}")
            for key, value in entry.items():
                print(f"{key}: {value}")
            print()
    else:
        print("Записів не знайдено.")


def clear_entries(entries):
    """Clear the list of entries"""
    entries.clear()
    save_entries(entries)
    print("Список записів очищено.")
