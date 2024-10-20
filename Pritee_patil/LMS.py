'''Problem 1: Library Management System
Create a program to manage a small library’s book collection. The program should:
Store book details (title, author, year, availability status) in a dictionary.
Implement functions to:
Add new books.
Update book availability when a book is borrowed or returned.
Display all available books using a for loop.
Use a while loop to continue accepting user input for various operations like adding or borrowing books.
Provide an option to search for books by title or author.'''

# Simple Library Management System
# Initial book details
library = {
    "book1": {
        "title": "Wings of Fire",
        "author": "ABC",
        "year": 2004,
        "availability_status": "y"  # corrected spelling
    },
    "book2": {
        "title": "Robbery",
        "author": "XYZ",
        "year": 2008,
        "availability_status": "n"  # corrected spelling
    }
}

def add_book(title, author, year):
    """Add a new book to the library."""
    library[title] = {
        'title': title,
        'author': author,
        'year': year,
        'availability_status': 'y'
    }
    print(f"Added: {title} by {author} ({year})")

def borrow_book(title):
    """Borrow a book from the library."""
    if title in library and library[title]['availability_status'] == 'y':
        library[title]['availability_status'] = 'n'
        print(f"You borrowed: {title}")
    else:
        print("Book not available.")

def return_book(title):
    """Return a borrowed book to the library."""
    if title in library:
        library[title]['availability_status'] = 'y'
        print(f"You returned: {title}")
    else:
        print("This book does not exist.")

def display_books():
    """Display all available books."""
    print("\nAvailable Books:")
    for details in library.values():
        if details['availability_status'] == 'y':
            print(f"- {details['title']} by {details['author']} ({details['year']})")

def main():
    while True:
        print("\n1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Available Books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            add_book(title, author, year)

        elif choice == '2':
            title = input("Enter book title to borrow: ")
            borrow_book(title)

        elif choice == '3':
            title = input("Enter book title to return: ")
            return_book(title)

        elif choice == '4':
            display_books()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


print(details)