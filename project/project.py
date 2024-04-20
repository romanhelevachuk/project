import datetime
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Article:
    def __init__(self, title, author, year, journal):
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) in {self.journal}"

class Magazine:
    def __init__(self, title, year, issue):
        self.title = title
        self.year = year
        self.issue = issue

    def __str__(self):
        return f"{self.title} ({self.year}, Issue {self.issue})"

class HomeLibrary:
    def __init__(self):
        self.books = []
        self.articles = []
        self.magazines = []

    def validate_year(self, year):
        current_year = datetime.datetime.now().year
        return year.isdigit() and 1 <= int(year) <= current_year

    def validate_length(self, text, max_length):
        return len(text) <= max_length

    def is_unique(self, title, author, collection):
        for item in collection:
            if item.title == title and item.author == author:
                return False
        return True

    def add_book(self, book):
        if self.is_unique(book.title, book.author, self.books):
            self.books.append(book)

    def add_article(self, article):
        if self.is_unique(article.title, article.author, self.articles):
            self.articles.append(article)

    def add_magazine(self, magazine):
        self.magazines.append(magazine)

    def remove_book(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                self.books.remove(book)
                break

    def remove_article(self, title, author):
        for article in self.articles:
            if article.title == title and article.author == author:
                self.articles.remove(article)
                break

    def remove_magazine(self, title, year, issue):
        for magazine in self.magazines:
            if magazine.title == title and magazine.year == year and magazine.issue == issue:
                self.magazines.remove(magazine)
                break

    def list_books(self):
        return "\n".join(str(book) for book in self.books)

    def list_articles(self):
        return "\n".join(str(article) for article in self.articles)

    def list_magazines(self):
        return "\n".join(str(magazine) for magazine in self.magazines)

    def search(self, query, search_type):
        if search_type == "book":
            return "\n".join(str(book) for book in self.books if query in str(book))
        elif search_type == "article":
            return "\n".join(str(article) for article in self.articles if query in str(article))
        elif search_type == "magazine":
            return "\n".join(str(magazine) for magazine in self.magazines if query in str(magazine))
        else:
            return "Недійсний тип пошуку. Будь ласка, спробуйте знову."

    def sort_books(self, by_year=True):
        return "\n".join(str(book) for book in sorted(self.books, key=lambda x: x.year, reverse=not by_year))

    def sort_articles(self, by_year=True):
        return "\n".join(str(article) for article in sorted(self.articles, key=lambda x: x.year, reverse=not by_year))

    def sort_magazines(self, by_year=True):
        return "\n".join(str(magazine) for magazine in sorted(self.magazines, key=lambda x: x.year, reverse=not by_year))

    def show_type(self, type):
        if type == "book":
            return self.list_books()
        elif type == "article":
            return self.list_articles()
        elif type == "magazine":
            return self.list_magazines()

    def run(self):
        while True:
            print("\nМеню Домашньої Бібліотеки:")
            print("1. Додати Книгу")
            print("2. Додати Статтю")
            print("3. Додати Журнал")
            print("4. Видалити Книгу")
            print("5. Видалити Статтю")
            print("6. Видалити Журнал")
            print("7. Переглянути Книги")
            print("8. Переглянути Статті")
            print("9. Переглянути Журнали")
            print("10. Пошук")
            print("11. Сортувати Книги")
            print("12. Сортувати Статті")
            print("13. Сортувати Журнали")
            print("14. Показати Тип Матеріалу")
            print("15. Вийти")
            choice = input("Введіть ваш вибір: ")

            if choice == "1":
                title = input("Введіть назву книги: ")
                author = input("Введіть ім'я автора: ")
                year = input("Введіть рік видання: ")
                if self.validate_year(year) and self.validate_length(title, 100) and self.validate_length(author, 100):
                    self.add_book(Book(title, author, year))
                    print("Книга додана успішно.")
                else:
                    print("Недійсний вхід. Будь ласка, спробуйте знову.")
            elif choice == "2":
                title = input("Введіть назву статті: ")
                author = input("Введіть ім'я автора: ")
                year = input("Введіть рік публікації: ")
                if self.validate_year(year) and self.validate_length(title, 100) and self.validate_length(author, 100):
                    self.add_article(Article(title, author, year))
                    print("Стаття додана успішно.")
                else:
                    print("Недійсний вхід. Будь ласка, спробуйте знову.")
            elif choice == "3":
                title = input("Введіть назву журналу: ")
                year = input("Введіть рік видання: ")
                issue = input("Введіть номер випуску: ")
                if self.validate_year(year) and self.validate_length(title, 100):
                    self.add_magazine(Magazine(title, year, issue))
                    print("Журнал доданий успішно.")
                else:
                    print("Недійсний вхід. Будь ласка, спробуйте знову.")
            elif choice == "4":
                title = input("Введіть назву книги для видалення: ")
                author = input("Введіть ім'я автора: ")
                self.remove_book(title, author)
                print("Книга видалена успішно.")
            elif choice == "5":
                title = input("Введіть назву статті для видалення: ")
                author = input("Введіть ім'я автора: ")
                self.remove_article(title, author)
                print("Стаття видалена успішно.")
            elif choice == "6":
                title = input("Введіть назву журналу для видалення: ")
                year = input("Введіть рік видання: ")
                issue = input("Введіть номер випуску: ")
                self.remove_magazine(title, year, issue)
                print("Журнал видалений успішно.")
            elif choice == "7":
                print(self.list_books())
            elif choice == "8":
                print(self.list_articles())
            elif choice == "9":
                print(self.list_magazines())
            elif choice == "10":
                search_type = input("Введіть тип матеріалу для пошуку (книга, стаття, журнал): ")
                query = input("Введіть запит для пошуку: ")
                print(self.search(query, search_type))
            elif choice == "11":
                print(self.sort_books())
            elif choice == "12":
                print(self.sort_articles())
            elif choice == "13":
                print(self.sort_magazines())
            elif choice == "14":
                print(self.show_type())
            elif choice == "15":
                print("Вихід...")
                break
            else:
                print("Недійсний вибір. Будь ласка, спробуйте знову.")


if __name__ == "__main__":
    library = HomeLibrary()
    library.run()




