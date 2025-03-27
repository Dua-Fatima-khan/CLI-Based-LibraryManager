import json

# File Handling Functions
def load_library():
    """Load the library from a file (if exists), otherwise return an empty list."""
    try:
        with open("library.txt", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save the library to a file."""
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)

# Load library at start
library = load_library()

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
    library.append(book)
    save_library(library)
    print("✅ Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(library)
    print("🗑️ Book removed successfully!")

def search_book():
    search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    
    if search_type == "1":
        title = input("Enter the title: ")
        results = [book for book in library if title.lower() in book["title"].lower()]
    elif search_type == "2":
        author = input("Enter the author: ")
        results = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("❌ Invalid choice!")
        return
    
    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("❌ No matching books found!")

def display_books():
    if not library:
        print("📭 No books in the library!")
        return
    
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"📚 Total books: {total_books}")
    print(f"✅ Percentage read: {percentage_read:.2f}%")

while True:
    print("\n📚 Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        print("Library saved. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
