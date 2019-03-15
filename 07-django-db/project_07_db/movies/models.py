from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.id}: {self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=150, default='')
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'''{self.id}: {self.title}, {self.audience}, {self.poster_url[:10]}\
            {self.description[:20]} - {self.genre}
            '''

class Score(models.Model):
    content = models.CharField(max_length=150, default='')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie} - {self.id}: {self.content[:10]}, {self.score}'