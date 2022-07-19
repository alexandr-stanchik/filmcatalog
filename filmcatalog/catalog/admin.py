from django.contrib import admin

from catalog.models import *

# admin.site.register(Director)
# admin.site.register(Film)
admin.site.register(Genre)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre')
    list_filter = ('year', 'genre')


# Register the Admin classes for BookInstance using the decorator

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(FilmInstance)
class FilmInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'viewer', 'status', 'mark')
    list_filter = ('status', 'viewer',)
# @admin.register(Genre)
# class GenreAdmin(admin.ModelAdmin):
# list_filter = ('name')
