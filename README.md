# Консольное приложение "Библиотека"
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/msrbl/library-console-app/blob/main/README-en.md)

**Консольное приложение "Библиотека"** — это инструмент на Python для управления локальной библиотекой. Приложение позволяет добавлять, удалять, искать книги, отображать список книг и обновлять их статус. Все данные хранятся в текстовом файле.

## Возможности

1. **Добавление книги**
   - Добавьте новую книгу, указав её название, автора и год издания.
   - Каждой книге автоматически присваивается уникальный ID и статус по умолчанию — "в наличии".

2. **Удаление книги**
   - Удалите книгу из библиотеки, используя её уникальный ID.

3. **Поиск книг**
   - Поиск книги по названию, автору или году издания.

4. **Отображение всех книг**
   - Просматривайте таблицу со списком книг, включая их ID, название, автора, год издания и статус.

5. **Изменение статуса книги**
   - Обновите статус книги (например, с "в наличии" на "выдана" и наоборот) с помощью её ID.

6. **Хранилище данных**
   - Книги сохраняются в текстовом файле (`storage.txt` или `storage_test.txt`). Если файл отсутствует, он создаётся автоматически.

---

## Описание классов

### `Book`
Представляет класс книги в библиотеке.

- **Атрибуты**:
  - `id` (int): Уникальный идентификатор книги.
  - `title` (str): Название книги.
  - `author` (str): Автор книги.
  - `year` (int): Год издания.
  - `status` (str): Статус книги, "в наличии" или "выдана".
  
- **Методы**:
  - `to_text()`: Преобразует атрибуты книги в форматированную строку для сохранения в файл.
  - `from_text(line)`: Создаёт объект `Book` из строки текста с разделителями `||`.

### `Library`
Управляет коллекцией книг и выполняет все операции, связанные с библиотекой.

- **Методы**:
  - `load_books_from_txt()`: Загружает книги из текстового файла. Если файл отсутствует, создаётся новый с заголовком.
  - `save_books_as_txt()`: Сохраняет текущее состояние библиотеки, перезаписывая файл.
  - `add_book(title, author, year)`: Добавляет новую книгу в библиотеку и сохраняет изменения.
  - `remove_book(book_id)`: Удаляет книгу из библиотеки по её ID.
  - `find_books(search_condition)`: Выполняет поиск книг по названию, автору или году издания.
  - `change_status(book_id)`: Изменяет статус книги. Допустимые значения: "в наличии", "выдана".
  - `display_books(books)`: Отображает указанный список книг в консоли.
  - `find_book_by_id(book_id)`: Находит книгу по уникальному идентификатору (вспомогательный метод).
  - `is_library_empty()`: Проверяет, пуста ли библиотека, и выводит сообщение (вспомогательный метод).

### Основная функциональность
Программа предоставляет меню для взаимодействия с библиотекой:
1. Добавить книгу
2. Удалить книгу
3. Искать книги
4. Показать все книги
5. Изменить статус книги
6. Выход

---

## Установка и настройка

### Требования
- Python 3.6 или выше.

### Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/msrbl/library-console-app
   cd library-console-app