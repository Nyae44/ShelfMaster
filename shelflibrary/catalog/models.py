from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(
        max_length = 200,
        unique = True,
        help_text = "Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )
    
    def __str__(self):
        """String representing the Model object"""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular genre instance"""
        return reverse('genre-detail', args=[str(self.id)])
    
class Book(models.Model):
    """Model representing a book (but not a copy of the book)"""
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('Author',on_delete = models.RESTRICT, null = True)
    # ForeignKey used because book can only have one author, but authors can have multiple books 
    # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(
        max_length = 1000, help_text = "Enter brief description of the book")
    isbn = models.CharField('ISBN', max_length = 13,
                            unique = True,
                              help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    
    # ManytoManyField is used because genre can contain many books. Books can cover many genres 
    # Genre class has already been defined so we can define the object above 
    
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this books"""
        return reverse('book-detail', args=[str(self.id)])    
    
class BookInstance(models.Model):
    """Model representing a specific copy of the book (that can be borrowed from the library)"""
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,
                          help_text = "Unique ID for this particular book across the whole library"
                          )
    book = models.ForeignKey('Book',on_delete = models.RESTRICT, null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True, blank = True)
    
    
    LOAN_STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On Loan'),
    ('a', 'Available'),
    ('r','Reserved')   
    )
    
    status = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS, 
        blank = True,
        default = 'm',
        help_text = "Book Availability",
    )
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self):
        """String for representing the Model object"""
        return f"{self.id} ({self.book.title})"
    
    
class Author(models.Model):
    """Model representing the author"""
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_death = models.DateField('died',null = True, blank = True)
    
    class Meta: 
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        """Returns the url of a particulat author instance"""
        
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """String representing the Model object"""
        return f"{self.last_name}, {self.first_name}"
    