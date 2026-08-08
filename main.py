import book_manager as bm 

def main():
    bm.initialize_file()

    while True:
        bm.display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bm.add_book()

        elif choice == "2":
            bm.view_books()

        elif choice == "3":
            bm.search_book()

        elif choice == "4":
            bm.update_book()

        elif choice == "5":
            bm.delete_book()

        elif choice == "6":
            print("\nThank you for using the Book Store Management System.")
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 6.")

main()
