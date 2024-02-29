from django.shortcuts import render
from Modelapp.forms import StudentsForm


def index(request):
    stud = StudentsForm
    return render(request, 'index.html', {'forms': stud})
