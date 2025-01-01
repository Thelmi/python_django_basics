class BookShelf:
	def __init__(self, *books):
		self.books = books
	def __str__(self):
			return f"BookShelf has {len(self.books)} books."

class book:
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return f"Book {self.name}"
		
book1 = book("The Lean Startup")
book2 = book("Zero to hero")

print(book1)
print(book2)

bookshelf = BookShelf(book1, book2)

print(bookshelf)