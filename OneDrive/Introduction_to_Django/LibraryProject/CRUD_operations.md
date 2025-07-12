# Create a Book instance

# Step 1: Open the Django shell
python manage.py shell

# Step 2: Run the following code in the shell
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

print(book)

# Expected Output:
# 1984 by George Orwell (1949)




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


