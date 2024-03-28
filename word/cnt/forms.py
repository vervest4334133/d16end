from django.forms import forms

from word.cnt.models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            'file',
        ]