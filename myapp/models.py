from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100, default='Other')  # Add a default value
    location = models.CharField(max_length=100, default='Unknown')  # Add a default value

    def __str__(self):
        return self.name

class Recruiter(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='recruiters', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Review(models.Model):
    company = models.ForeignKey(Company, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.company.name}'

class RecruiterReview(models.Model):
    recruiter = models.ForeignKey(Recruiter, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.recruiter.name}'
