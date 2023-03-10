from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.
from Eportfolio.models import *


def index(request):
    t = Subject.objects.all()
    return render(request, "professor/prof.html",{
        'subjects' : t
    })
    
    
@csrf_exempt
def subject(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    # data = json.loads(request.body)
    subjectCode = request.POST['subjectCode']
    subName = request.POST['subjectName']
    fName = request.POST['facultyName']
    units = request.POST['units']
    
    studentSubject = Subject(subjectCode = subjectCode,subjectName = subName, facultyName= fName,units=units)
    studentSubject.save()
    
    return JsonResponse({"message": "Email sent successfully."}, status=201)    


def showSubject(request):
    subjects = Subject.objects.all()
    return JsonResponse([sub.serialize() for sub in subjects], safe=False)
    
    