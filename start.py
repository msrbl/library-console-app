from classes import Library

def show_menu():
    """Показывает меню и возвращает выбранное действие."""
    options = {
        "1": "Добавить книгу",
        "2": "Удалить книгу",
        "3": "Искать книги",
        "4": "Показать все книги",
        "5": "Изменить статус книги",
        "6": "Выход"
    }

    print("\nНажмите Enter для продолжения")
    input()
    
    for key, value in options.items():
        print(f"{key}. {value}")
    return input("Выберите желаемое действие (введите цифру): ")

def add(library):
    title = input("\nВведите название книги: ")
    author = input("Введите автора книги: ")

    try:
        year = int(input("Введите год издания книги: "))
        library.add_book(title, author, year)
    except ValueError:
        print("Год должен быть числом.")

def delete(library):
    try:
        book_id = int(input("\nВведите ID книги: "))
        library.remove_book(book_id)
    except ValueError:
        print("ID должен быть числом.")

def find(library):
    search_term = input("\nВведите строку для поиска (название, фамилия автора или год издания): ")
    results = library.find_books(search_term)

    if results:
        library.display_books(results)
    else:
        print("Книги не найдены.")

def change_status(library):
    try:
        book_id = int(input("\nВведите ID книги: "))
        library.change_status(book_id)
    except ValueError:
        print("ID должен быть числом.")

def main():
    """
    Основная функция консольного приложения.

    Осуществляет выбор действия через метод show_menu().
    Также обрабатывает ошибки и неправильный ввод.
    """

    keyword = input("\nДля запуска приложения с тестовой библиотекой напишите ключевое слово 'test'\n")
    print("\nЗагружаем библиотеку из файла.")
    if keyword == "test":
        library = Library("storage_test.txt")
    else:
        library = Library("storage.txt")

    while True:
        action = show_menu()

        if action == "1":
            add(library)

        elif action == "2":
            delete(library)

        elif action == "3":
            find(library)

        elif action == "4":
            library.display_books(library.books)

        elif action == "5":
            change_status(library)

        elif action == "6":
            print("Выход из программы.")
            break

        else:
            print("\nНекорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()