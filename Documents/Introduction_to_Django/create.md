# Create a Book instance

# Step 1: Open the Django shell
python manage.py shell

# Step 2: Run the following code in the shell
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

print(book)

# Expected Output:
# 1984 by George Orwell (1949)
