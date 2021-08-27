from django import forms
from django.forms import fields, models
from .models import *

class BookForm(forms.Form):
    class Meta:
        model = AddBookModel
        fields = ['id','bname','aname','price']
    
class SearchForm(forms.Form):
    title = forms.CharField(max_length=40)