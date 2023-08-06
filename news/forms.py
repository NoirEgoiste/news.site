from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, TimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'annons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name article',

            }),
            'annons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement',

            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text',

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication Date',
            }),
        }
