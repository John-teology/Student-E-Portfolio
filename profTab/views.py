from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse 


# Create your views here.
from Eportfolio.models import *


def index(request):
    t = Subject.objects.all()
    if request.method == "POST":
        subjectCode = request.POST['SubjectCode']
        subjectName = request.POST['subjectName']
        facultyName = request.POST['facultyName']
        units = request.POST['units']

        studentSubject = Subject(subjectCode = subjectCode,subjectName = subjectName, facultyName= facultyName,units=units)
        
        studentSubject.save()
        return HttpResponseRedirect(reverse('indexProf'))
    return render(request, "professor/prof.html",{
        'subjects' : t
    })