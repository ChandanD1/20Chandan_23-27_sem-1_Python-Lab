# Write a program Design the Library catalogue system using inheritance take
# base class (library item) and derived class (Book, DVD & Journal) Each derived
# class should have unique attribute and methods and system should support Check
# in and check out the system. (Using Inheritance and Method overriding)

class LibraryItem:
    def __init__(self, title, author, item_id, copies_sold):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.copies_sold = copies_sold
        self.availability = True

    def display_info(self):
        print(f"{self.item_id}. {self.title} by {self.author} ({'Available' if self.availability else 'Not Available'})")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, copies_sold):
        super().__init__(title, author, item_id, copies_sold)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"   Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration, copies_sold):
        super().__init__(title, director, item_id, copies_sold)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"   Director: {self.director}, Duration: {self.duration} minutes")


class Journal(LibraryItem):
    def __init__(self, title, author, item_id, volume, copies_sold):
        super().__init__(title, author, item_id, copies_sold)
        self.volume = volume

    def display_info(self):
        super().display_info()
        print(f"   Volume: {self.volume}")


def display_catalog(items):
    print("\nLibrary Catalogue:")
    for item in items:
        item.display_info()


books = [
    Book("The Catcher in the Rye", "J.D. Salinger", "B001", "Fiction", 100),
    Book("To Kill a Mockingbird", "Harper Lee", "B002", "Classic", 150),
    Book("The Hobbit", "J.R.R. Tolkien", "B003", "Fantasy", 120),
]

dvds = [
    DVD("Inception", "Christopher Nolan", "D001", 148, 200),
    DVD("The Shawshank Redemption", "Frank Darabont", "D002", 142, 180),
    DVD("The Dark Knight", "Christopher Nolan", "D003", 152, 220),
]

journals = [
    Journal("Nature", "Various", "J001", "Vol. 587", 50),
    Journal("Science", "Various", "J002", "Vol. 374", 60),
]

while True:
    print("\nChoose an option:")
    print("1. View Books")
    print("2. View DVDs")
    print("3. View Journals")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_catalog(books)
    elif choice == "2":
        display_catalog(dvds)
    elif choice == "3":
        display_catalog(journals)
    elif choice == "4":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

    item_id = input("Enter the item ID you want to borrow (or '0' to go back): ")
    
    if item_id == "0":
        continue

    quantity = int(input("Enter the quantity you want to borrow: "))

    selected_item = None
    catalog = books + dvds + journals
    for item in catalog:
        if item.item_id == item_id:
            selected_item = item
            break

    if selected_item and selected_item.availability and quantity <= selected_item.copies_sold:
        selected_item.availability = False
        print(f"\n{quantity} {selected_item.title}(s) successfully borrowed.")
    else:
        print("\nInvalid selection or not enough copies available. Please try again.")
