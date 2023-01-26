from django.db import models

# Create your models here.

class SurveyForm(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    date = models.DateField()
    # Define the options into the form