from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, null=True, blank=True, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.rating} stars'

