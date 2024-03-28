from django.forms import forms

from word.cnt.models import Word


class PostForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            'file',
        ]