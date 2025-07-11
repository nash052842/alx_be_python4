# Update the title of the book

# Step 1: Open the Django shell
python manage.py shell

# Step 2: Run the following code in the shell
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

# Expected Output:
# Nineteen Eighty-Four
