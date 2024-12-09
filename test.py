import unittest
from classes import Library
import os

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        """Создаем тестовую библиотеку."""
        self.test_file = "test_library.txt"
        self.library = Library(self.test_file)
        self.library.books = []  # Очищаем библиотеку
        self.library.save_books_as_txt()

    def tearDown(self):
        """Удаляем тестовый файл после каждого теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Проверяем добавление книги."""
        self.library.add_book("Test Book", "Test Author", 2022)
        
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_remove_book(self):
        """Проверяем удаление книги."""
        self.library.add_book("Test Book", "J.K.Author", 2022)
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)

        self.assertEqual(len(self.library.books), 0)

    def test_find_books_by_title(self):
        """Проверяем поиск книги по названию."""
        self.library.add_book("Unique Title", "J.K.Author", 2020)
        results = self.library.find_books("Unique")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Unique Title")

    def test_find_books_by_author(self):
        """Проверяем поиск книги по автору."""
        self.library.add_book("Book", "J.K.Special", 2020)
        results = self.library.find_books("Special")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "J.K.Special")

    def test_find_books_by_year(self):
        """Проверяем поиск книги по году издания."""
        self.library.add_book("Book", "J.K.Author", 2020)
        results = self.library.find_books("2020")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, 2020)

    def test_change_status(self):
        """Проверяем изменение статуса книги."""
        self.library.add_book("Book", "J.K.Author", 2020)
        self.library.books[0].status = "выдана"
        self.library.save_books_as_txt()

        self.assertEqual(self.library.books[0].status, "выдана")

    def test_load_books_from_file(self):
        """Проверяем загрузку книг из файла."""
        self.library.add_book("Book1", "J.K.Author1", 2001)
        self.library.add_book("Book2", "J.K.Author2", 2002)
        self.library = Library(self.test_file)

        self.assertEqual(len(self.library.books), 2)

if __name__ == "__main__":
    unittest.main()