from django import forms
from board.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', )