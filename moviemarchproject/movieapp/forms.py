from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','desc','category','date','actors','trailer_link','img']




class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


