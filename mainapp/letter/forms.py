from django import forms
from .models import ChristmasLetter


class ChristmasLetterForm(forms.ModelForm):
    class Meta:
        model = ChristmasLetter
        fields = ('title', 'content', 'signature')
        labels = {'title': 'Title',
                  'content': 'Content',
                  'signature': 'Signature'}
