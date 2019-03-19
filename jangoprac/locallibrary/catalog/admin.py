from django.contrib import admin
from catalog.models import Book, Author, Genre, BookInstance
# Register your models here.

# Define the admin class

# class AuthorsInstanceInline(admin.TabularInline):
#     model = Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
    # inlines = [AuthorsInstanceInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BooksInstanceInline]

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','imprint','due_back','id')
    list_filter = ('status','due_back')

    fieldsets = (
        (None, {
            'fields':('book','imprint','id')
        }),
        ('Availability', {
            'fields':('status','due_back')
        }),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)