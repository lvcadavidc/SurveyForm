from django import forms
from .models import SurveyForm

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



class Form(forms.Form):
    class Meta:
        model = SurveyForm
        fields = (
            'name', 
            'email',
            'experience_years',
            'role',
            'design',
            'full_stack', 
            'front_end', 
            'back_end', 
            'customer_support', 
            'devOps',
            'sales_marketing',
            'management_finance',
            'product',
            'other_remote',
            'like_survey',
        )

    name = forms.CharField()
    email = forms.EmailField()
    experience_years = forms.IntegerField()
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,    
    )
    #Interests checkboxes
    design = forms.BooleanField()
    full_stack = forms.BooleanField()
    front_end = forms.BooleanField()
    back_end = forms.BooleanField()
    customer_support = forms.BooleanField()
    devOps = forms.BooleanField()
    sales_marketing = forms.BooleanField()
    management_finance = forms.BooleanField()
    product = forms.BooleanField()
    other_remote = forms.BooleanField()

    #Radio buttons
    like_survey = forms.ChoiceField(
        choices=YES_OR_NO,
    )
    