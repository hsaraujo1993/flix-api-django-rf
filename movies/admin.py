from multiprocessing.resource_tracker import register

from django.contrib import admin
from movies.models import Movie

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'genre', 'release_date')
