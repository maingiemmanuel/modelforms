from django import forms
from Modelapp.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
