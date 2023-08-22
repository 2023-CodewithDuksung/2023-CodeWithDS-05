from django import forms
from .models import Challenge

class ChallengeForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='챌린지 제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-input',
                'placeholder':'무슨 챌린지에 도전할까요?'
            }
        )
    )

    class Meta:
        model = Challenge
        fields = ('title', 'category')