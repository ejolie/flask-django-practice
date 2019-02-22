from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, unique=True)
    audience = models.IntegerField(validators=[MinValueValidator(0)])
    genre = models.CharField(max_length=20)
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    posterurl = models.URLField()
    description = models.TextField()
    
    def __str__(self):
        return f'<{self.title} | {self.audience} | {self.genre} | {self.score} | {self.posterurl} | {self.description}>'
        
    def __repr__(self):
        return f'<{self.title} | {self.audience} | {self.genre} | {self.score} | {self.posterurl} | {self.description}>'