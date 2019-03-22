from django import forms
from .models import Genre, Movie, Score

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'audience', 'poster_url', 'description', 'genre']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'audience': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }   
            ),
            'poster_url': forms.URLInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        
class ScoreModelForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['content', 'score']
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'score': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }   
            ),
        }