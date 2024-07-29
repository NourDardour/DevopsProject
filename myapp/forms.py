from django import forms
from .models import Company, Review, Recruiter, RecruiterReview

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'industry']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['company', 'rating', 'comment']

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['name', 'company', 'email']

class RecruiterReviewForm(forms.ModelForm):
    class Meta:
        model = RecruiterReview
        fields = ['recruiter', 'rating', 'comment']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
