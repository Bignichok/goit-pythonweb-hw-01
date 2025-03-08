from abc import ABC, abstractmethod
from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} - {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> List[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> List[Book]:
        books = self.library.show_books()

        if books:
            for book in books:
                print(book)
        else:
            print("No books in library")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter title: ").strip()
                author = input("Enter author: ").strip()
                year = int(input("Enter year: ").strip())
                manager.add_book(title, author, year)

            case "remove":
                title = input("Enter title: ").strip()
                manager.remove_book(title)

            case "show":
                manager.show_books()

            case "exit":
                break

            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
