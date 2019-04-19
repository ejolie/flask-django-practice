from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(),
    )
    value = forms.IntegerField(
        label='평점',
        widget=forms.NumberInput(),
    )

    class Meta:
        model = Score
        fields = ['content', 'value']