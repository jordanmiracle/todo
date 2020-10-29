from django.forms import ModelForm
from .models import Todo
from django import forms

categories = [
    ('personal', 'PERSONAL'),
    ('school', 'school'),
    ('work', 'WORK'),
    ('shopping', 'SHOPPING'),
    ('appointments', 'APPOINTMENTS')
]


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
    categoryfield = forms.ChoiceField(choices=categories)