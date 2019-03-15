from django.contrib import admin
from .models import Genre, Score, Movie

admin.site.register(Genre)
admin.site.register(Score)
admin.site.register(Movie)