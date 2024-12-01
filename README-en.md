# Library Console Application
[![ru](https://img.shields.io/badge/lang-ru-red.svg)](https://github.com/msrbl/library-console-app/edit/main/README.md)

**Library Console Application** is a Python-based tool for managing a local library. The application allows users to add, remove, search, display, and update the status of books stored in a text file. 

## Features

1. **Add a Book**
   - Add a new book by providing its title, author, and year of publication.
   - Each book is assigned a unique ID and the default status "в наличии".

2. **Remove a Book**
   - Delete a book from the library using its unique ID.

3. **Search for Books**
   - Search for books by title, author, or year of publication.

4. **Display All Books**
   - Display a tabular list of given books with their ID, title, author, year, and status.

5. **Change Book Status**
   - Update the status of a book (e.g., from "в наличии" to "выдана" and vice versa) using its ID.

6. **Persistent Storage**
   - Books are stored in a text file (`storage.txt` or `storage_test.txt`). If the file doesn't exist, it is created automatically with a header row.

---

## Class Overview

### `Book`
Represents a book in the library.

- **Attributes**:
  - `id` (int): Unique identifier for the book.
  - `title` (str): Title of the book.
  - `author` (str): Author of the book.
  - `year` (int): Year of publication.
  - `status` (str): Status of the book, either "в наличии" or "выдана".
  
- **Methods**:
  - `to_text()`: Converts book attributes to a formatted string for saving to a file.
  - `from_text(line)`: Creates a `Book` object from a string of text with || delimiters.

### `Library`
Manages the collection of books and handles all operations related to the library.

- **Methods**:
  - `load_books_from_txt()`: Loads books from text file. Creates the file with a header if it doesn't exist.
  - `save_books_as_txt()`: Saves the current state of the library and overwriting it.
  - `add_book(title, author, year)`: Adds a new book to the library and saves it.
  - `remove_book(book_id)`: Removes a book from the library by its ID.
  - `find_books(search_condition)`: Search for books in the library by title, author, or year.
  - `change_status(book_id)`: Changes the status of the book. Valid values are “в наличии”, “выдана”.
  - `display_books(books)`: Displays a specified list of books in the console.
  - `find_book_by_id(book_id)`: Search for a book by unique identifier (helper method).
  - `is_library_empty()`: Checks if the library is empty and prints a message if so (helper method).

### Main Functionality
The program provides a menu-based system for interacting with the library:
1. Add Book
2. Remove Book
3. Search Books
4. Display All Books
5. Change Book Status
6. Exit

---

## Installation and Setup

### Prerequisites
- Python 3.6 or higher.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/msrbl/library-console-app
   cd library-console-app
2. Run the script in the terminal:
   ```bash
   python library.py
