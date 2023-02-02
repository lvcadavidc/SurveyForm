from django.db import models

# Create your models here.

#Iterable for  role choices
ROLE_CHOICES = [
        ("", "Select your current role"),
        ("1", "Student"),
        ("2", "Full time Job"),
        ("3", "Part Time Job"),
        ("4", "Freelance"),
        ("5", "Prefer not to say"),
        ("6", "Other")
    ]

#Iterable for liked_survey options
YES_OR_NO = [
    ("", "Select"),
    ('yes', 'Yes, I like it!'),
    ('no', 'No, it could be better')
]


class SurveyForm(models.Model):
    name = models.TextField()
    email = models.EmailField()
    experience_years = models.IntegerField()
    role = models.CharField(
        choices=ROLE_CHOICES,
        max_length=35,
        default="",        
    )
    #Interests checkboxes
    design = models.BooleanField()
    full_stack = models.BooleanField()
    front_end = models.BooleanField()
    back_end = models.BooleanField()
    customer_support = models.BooleanField()
    devOps = models.BooleanField()
    sales_marketing = models.BooleanField()
    management_finance = models.BooleanField()
    product = models.BooleanField()
    other_remote = models.BooleanField()

    #Radio buttons
    like_survey = models.CharField(
        choices=YES_OR_NO,
        max_length=20,
        default=""
    )

