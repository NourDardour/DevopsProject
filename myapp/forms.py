from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
