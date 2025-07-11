# Retrieve and display the book's attributes

# Step 1: Open the Django shell
python manage.py shell

# Step 2: Run the following code in the shell
from bookshelf.models import Book

book = Book.objects.get(title="1984")

print(book.title)
print(book.author)
print(book.publication_year)

# Expected Output:
# 1984
# George Orwell
# 1949
