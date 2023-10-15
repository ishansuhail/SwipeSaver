from django import forms
#from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'rating']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
