from django import forms

class CustomDateWidget(forms.DateInput):
    input_type = 'date'