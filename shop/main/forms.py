from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feed, History
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateInput, Select

User = get_user_model()
class FeedForm(ModelForm):
    class Meta:
        model=Feed
        fields=['fio','text','date']

        widgets={
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }

class HistForm(ModelForm):
    class Meta:
        model=History
        fields=['tovar','razmer','kol','email','fio','date','text']

        widgets = {
            "tovar": Select(attrs={
                'class': 'form-control',
            }),
            "razmer": Select(attrs={
                'class': 'form-control',
            }),
            "kol": TextInput(attrs={
                'class': 'form-control',
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
            }),
            "fio": TextInput(attrs={
                'class': 'form-control',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
            }),
        }



class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

