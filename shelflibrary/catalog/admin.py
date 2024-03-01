from django.contrib import admin
from .models import Genre, Language, Book, BookInstance, Author

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)

# Changing how a model is displayed
# Define the admin class

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model

admin.site.register(Author,AuthorAdmin)

    
# To add associated records at the same time we declare inlines
# Inlines can either be Tabularinlines(horizontal) or stackedinlines(vertical)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
# Register the admin classes for book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    inlines = [BooksInstanceInline]
# Register the admin classes for book instances using the decorator 

@admin.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
    # To filter items to be displayed we use the list_filter attribute
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    # To add sections we use fieldsets 
    # Each section has its own title or none if you dont want to set a title 
    fieldsets = (
        (None, {
            'fields' : ('book', 'imprint', 'id')
        }),
        ('Availability',{
            'fields' : ('status','due_back', 'borrower')
        })
    )
