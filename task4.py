class Book:
    def __init__(b, title, author, year_published):
        b.title = title
        b.author = author
        b.year_published = year_published

    def describe(b):
        print(f"{b.title}' by {b.author}, published in {b.year_published}.")
        


book1 = Book("Think and Grow Rich", "Napoleon Hill", 1937)
book2 = Book("The 48 Laws of Power", "Robert Greene", 1998)
book3 = Book("The Subtle Art of Not Giving a Fuck", "Lenard Balintong", 1969)

book1.describe()
book2.describe()
book3.describe()
