from django import forms
from .models import students

class student_Form(forms.ModelForm):
    class Meta:
        model=students
        fields= "__all__"