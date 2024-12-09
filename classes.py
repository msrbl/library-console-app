class Book:
    """
    Класс для представления книги.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания.
        status (str): Статус книги ("в наличии" или "выдана").
    """
    def __init__(self, book_id, title, author, year, status="в наличии"):
        """Инициализатор класса. Присваивает переданные значения к переменным класса."""
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_text(self):
        """Преобразует атрибуты книги в форматированную строку для сохранения в файл."""
        return f"{self.id:<4}|| {self.title:<40}|| {self.author:<30}|| {self.year:<6}|| {self.status:<9}"

    @staticmethod
    def from_text(line):
        """Создает объект книги из строки текста с разделителями ||."""
        try:
            parts = [part.strip() for part in line.split("||")]
            if len(parts) == 5:
                return Book(int(parts[0]), parts[1], parts[2], int(parts[3]), parts[4])
            else:
                return None
        except ValueError:
            return None

class Library:
    """
    Класс для представления библиотеки.
    
    Атрибуты:
        storage_file (str): Путь к файлу хранения библиотеки.
        books [Book]: Массив хранения объектов класса Book.
    """
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.books = self.load_books_from_txt()

    def load_books_from_txt(self):
        """Загружает базу данных книг из текстового файла."""
        books = []
        try:
            with open(self.storage_file, "r", encoding="utf-8") as txt_file:
                for line in txt_file:
                    if line.startswith("ID") or line.startswith("-"):
                        continue

                    book = Book.from_text(line)
                    if book:
                        books.append(book)
        except FileNotFoundError:
            with open(self.storage_file, "w", encoding="utf-8") as txt_file:
                pass
            pass
        return books

    def save_books_as_txt(self):
        """Перезаписывает и сохраняет файл хранилища книг."""
        with open(self.storage_file, "w+", encoding="utf-8") as txt_file:
            header = f"{'ID':<4}   {'Название':<40}   {'Автор':<30}   {'Год':<6}   {'Статус':<9}"
            txt_file.write(header + "\n")
            txt_file.write("-" * len(header) + "\n")

            for book in self.books:
                txt_file.write(book.to_text() + "\n")

    def add_book(self, title, author, year):
        """Добавляет новую книгу в библиотеку."""
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)

        self.save_books_as_txt()

        print(f"\nКнига добавлена: {new_book.title} (ID: {new_book.id})")

    def remove_book(self, book_id):
        """Удаляет книгу по уникальному идентификатору."""
        if self.is_library_empty():
            return
        else:
            book = self.find_book_by_id(book_id)
            if book:
                self.books.remove(book)
                self.save_books_as_txt()

                print(f"\nКнига удалена: {book.title} (ID: {book.id})")
            else:
                print(f"\nКнига с ID {book_id} не найдена.")

    def find_books(self, search_condition):
        """
        Поиск книг в библиотеке.
        Если условие поиска совпадает со словом из названия,
        фамилией автора или это год издания книги, добавляет
        книгу к выводу и выводит все такие экземпляры.
        """
        if self.is_library_empty():
            return
        else:
            results = []
            search_condition = search_condition.lower().strip().split(' ')

            for book in self.books:
                for search_word in search_condition:
                    if any(word.lower() == search_word for word in book.title.split()):
                        results.append(book)
                    elif search_word == book.author.split('.')[-1].lower():
                        results.append(book)
                    elif search_word == str(book.year):
                        results.append(book)
            return results

    def change_status(self, book_id):
        """Изменяет статус книги. Допустимые значения - "в наличии", "выдана"."""
        if self.is_library_empty():
            return
        else:
            book = self.find_book_by_id(book_id)
            if book:
                status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                if status in ["в наличии", "выдана"]:
                    book.status = status
                    self.save_books_as_txt()

                    print(f"\nСтатус книги изменён: {book.title} (ID: {book.id}) — {status}")
                else:
                    print("\nНекорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
            else:
                print(f"\nКнига с ID {book_id} не найдена.")

        
    def find_book_by_id(self, book_id):
        """Поиск книги по уникальному идентификатору."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def display_books(self, books):
        """Осуществляет отображение определенного списка книг в консоли."""
        if not books:
            print(f"\nКниги не найдены.")
            return

        header = f"\n{'ID':<4}|| {'Название':<40}|| {'Автор':<30}|| {'Год':<6}|| {'Статус':<9}"
        print(header)

        lengths = header.strip().split("||")
        lengths = ["-" * len(length) for length in lengths]
        separator = "||".join(lengths)
        print(separator)

        for book in books:
            print(book.to_text())

    def is_library_empty(self):
        """Проверяет, пуста ли библиотека, и выводит сообщение, если это так."""
        if not self.books:
            print("\nБиблиотека пуста. Для добавления книг выберите действие 'Добавить книгу'.")
            return True
        return False