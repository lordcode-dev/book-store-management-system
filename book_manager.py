import csv
import os
from tabulate import tabulate

FILE_NAME = "books.csv"
FIELDNAMES = ["ID", "Title", "Author", "Price"]
# Create the CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
# Read all books from the CSV file
def read_books():
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
# Validate Book ID
def get_valid_id():
    while True:
        book_id = input("Enter Book ID: ").strip()

        if book_id and book_id.isalnum():
            return book_id

        print("Invalid input. Book ID must contain only letters and numbers.")
# Validate Title or Author
def get_valid_text(field_name):
    while True:
        value = input(f"Enter {field_name}: ").strip()

        if value and all(char.isalpha() or char.isspace() for char in value):
            return value

        print(
            f"Invalid input. {field_name} must contain only alphabetic characters."
        )
# Validate Price
def get_valid_price():
    while True:
        price = input("Enter Price: ").strip()

        try:
            price = float(price)

            if price >= 0:
                return f"{price:.2f}"

            print("Invalid input. Price cannot be negative.")

        except ValueError:
            print("Invalid input. Price must be a numeric value.")
# Check whether a book ID already exists
def book_exists(book_id):
    books = read_books()

    for book in books:
        if book["ID"] == book_id:
            return True

    return False
# Add a new book
def add_book():
    print("\n========== ADD BOOK ==========")

    while True:
        book_id = get_valid_id()

        if book_exists(book_id):
            print("Invalid input. A book with this ID already exists.")
        else:
            break

    title = get_valid_text("Title")
    author = get_valid_text("Author")
    price = get_valid_price()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writerow({
            "ID": book_id,
            "Title": title,
            "Author": author,
            "Price": price
        })

    print("\nBook added successfully!")
# View all books
def view_books():
    print("\n========== VIEW BOOKS ==========")

    books = read_books()

    if not books:
        print("No books found.")
        return

    table = []

    for book in books:
        table.append([
            book["ID"],
            book["Title"],
            book["Author"],
            book["Price"]
        ])

    print(tabulate(
        table,
        headers=["ID", "Title", "Author", "Price"],
        tablefmt="grid"
    ))
# Search for a book by ID
def search_book():
    print("\n========== SEARCH BOOK ==========")

    book_id = get_valid_id()
    books = read_books()

    for book in books:
        if book["ID"] == book_id:
            table = [[
                book["ID"],
                book["Title"],
                book["Author"],
                book["Price"]
            ]]

            print(tabulate(
                table,
                headers=["ID", "Title", "Author", "Price"],
                tablefmt="grid"
            ))

            return

    print("Book not found.")
# Update a book
def update_book():
    print("\n========== UPDATE BOOK ==========")

    book_id = get_valid_id()
    books = read_books()

    book_found = False

    for book in books:
        if book["ID"] == book_id:
            book_found = True

            print("\nEnter the new book details:")

            new_title = get_valid_text("Title")
            new_author = get_valid_text("Author")
            new_price = get_valid_price()

            book["Title"] = new_title
            book["Author"] = new_author
            book["Price"] = new_price

            break

    if not book_found:
        print("Book not found.")
        return

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writeheader()
        writer.writerows(books)

    print("Book updated successfully!")
# Delete a book
def delete_book():
    print("\n========== DELETE BOOK ==========")

    book_id = get_valid_id()
    books = read_books()

    new_books = []
    book_found = False

    for book in books:
        if book["ID"] == book_id:
            book_found = True
        else:
            new_books.append(book)

    if not book_found:
        print("Book not found.")
        return

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writeheader()
        writer.writerows(new_books)

    print("Book deleted successfully!")
# Display the main menu
def display_menu():
    print("\n")
    print("========================================")
    print("       BOOK STORE MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")
    print("========================================")
#Exit the program
def exit():
    print("\nThank you for using the Book Store Management System.")
    print("Goodbye!")
#for invalid input
def invalid():
    print("Invalid input. Please enter a number from 1 to 6.")
