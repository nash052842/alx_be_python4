# Delete the book and confirm deletion

# Step 1: Open the Django shell
python manage.py shell

# Step 2: Run the following code in the shell
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm the book is deleted
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>
