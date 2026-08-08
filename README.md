# 📚 Book Store Management System

A console-based Python application designed to manage book records efficiently using a CSV file. The system allows users to perform CRUD (Create, Read, Update, Delete) operations while validating user input to maintain accurate and consistent data.

## 📌 Project Description

The **Book Store Management System** is a simple command-line application developed using Python. It stores book information in a `books.csv` file and provides an easy-to-use menu-driven interface for managing book records.

Users can add, view, search, update, and delete books. The application also performs input validation to ensure that users enter information in the correct format.

## ✨ Features

### 1. Add Book

* Allows users to manually enter book details.
* Required details:

  * Book ID
  * Title
  * Author
  * Price
* Validates user input before storing the record.
* Saves the book information to `books.csv`.

### 2. View Books

* Displays all stored books.
* Uses the `tabulate` library to display records in a clear table.
* Displays a message if no books are available.

### 3. Search Book

* Allows users to search for a book using its ID.
* Displays the matching book in a table if found.
* Displays an appropriate message if the book does not exist.

### 4. Update Book

* Allows users to update an existing book by entering its ID.
* Validates the new information before updating the record.
* Saves the updated information to the CSV file.

### 5. Delete Book

* Allows users to delete a book using its ID.
* Removes the selected book from the CSV file.
* Displays a message if the specified book is not found.

### 6. Exit

* Allows users to exit the application safely and gracefully.

## 🛠️ Technologies Used

| Technology           | Purpose                                |
| -------------------- | -------------------------------------- |
| **Python**           | Main programming language              |
| **CSV**              | File format used to store book records |
| **csv Library**      | Reading and writing CSV data           |
| **tabulate Library** | Displaying records in table format     |

## 📂 Project Structure

```text
book-store-management-system/
│
├── main.py
├── book_manager.py
├── books.csv
├── requirements.txt
├── LICENSE
└── README.md
```

### File Description

* `main.py` — Contains the main Python application.
* `book_manager.py` — contains all functions. 
* `books.csv` — Stores the book records.
* `requirements.txt` — Contains the required external Python libraries.
* `LICENCE` — contains the right to the code via MIT.
* `README.md` — Contains the project documentation.
## ⚙️ How It Works

1. When the program starts, it checks whether `books.csv` exists.
2. If the file does not exist, the system creates it.
3. Users interact with the application through a menu-driven interface.
4. The system validates user input before adding or updating records.
5. Book records are read from and written to the CSV file.
6. Users can perform CRUD operations on the stored records.
7. The `tabulate` library displays book information in a formatted table.

## 🔍 Input Validation

The system validates the following information:

* **Book ID:** Must contain only letters and numbers.
* **Title:** Must contain alphabetic characters and spaces.
* **Author:** Must contain alphabetic characters and spaces.
* **Price:** Must be a valid numeric value.
* Required fields cannot be left empty.

This validation helps maintain the accuracy and consistency of the stored book records.

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/lordcode-dev/book-store-management-system.git
```

### 2. Navigate to the project directory

```bash
cd book-store-management-system
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

Or install `tabulate` directly:

```bash
pip install tabulate
```

> The `csv` library is included with Python's standard library and does not need to be installed separately.

## ▶️ Running the Program

Run the following command:

```bash
python main.py
```

The program will display a menu similar to:

```text
========================================
       BOOK STORE MANAGEMENT SYSTEM
========================================

1. Add Book
2. View Books
3. Search Book
4. Update Book
5. Delete Book
6. Exit

Enter your choice:
```

## 📊 Example Output

```text
+------+----------------+----------------+--------+
| ID   | Title          | Author         | Price  |
+------+----------------+----------------+--------+
| B001 | Python Basics  | John Smith     | 25.50  |
| B002 | Java Basics    | Jane Brown     | 30.00  |
+------+----------------+----------------+--------+
```

## 🎯 Use Cases

This project is ideal for:

* Small bookstores that need a simple book-record management system.
* Students learning Python programming.
* Learning CSV file handling.
* Understanding user input validation.
* Practicing CRUD operations.
* Learning data manipulation in Python.
* Understanding how a menu-driven console application works.
## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for the full license text.
## 👥 Project Team

This project was developed by **Group 8** as a collaborative Python project.

**Group:**  G
**GitHub:** https://github.com/lordcode-dev/book-store-management-system

## 📄 Project Status

**Completed**

This project fulfills the specified requirements for managing book records using Python, CSV file handling, input validation, and the `tabulate` library.
