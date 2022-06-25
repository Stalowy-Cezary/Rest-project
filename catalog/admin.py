from django.contrib import admin
from .models import Book, Genre, BookInstance, Author, Language

#admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)
#admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book
    classes = ['collapse']
    search_fields = ('title')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    search_fields = ('last_name', 'first_name')
    fieldsets = (
    (None, {
        'fields' : ('last_name', 'first_name')
    }),
    ('Advanced options', {
        'classes': ('collapse',),
        'fields': ('date_of_birth', 'date_of_death'),
    }))

    inlines = [
        BookInline,
    ]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    show_change_link = True #TODO

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [
        BookInstanceInline,
    ]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ['id', 'book', 'status', 'due_back']
    #fields = ['id', 'book', 'status', 'due_back']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass



