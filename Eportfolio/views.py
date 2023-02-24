from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profileForm'))
    return render(request,"landing.html")
 
 
# @login_required  
def demographicForm(request):
    userid = User.objects.get(username = request.user)
    if (Studentprofile.objects.filter(userID = userid).count() > 0):
        studentN = Studentprofile.objects.get(userID=userid)
        return HttpResponseRedirect(reverse('studentProfile',args=(studentN.studentNumber,)))
    if request.method == "POST":
        studentNumber = request.POST['studentNumber']
        first = request.user.first_name
        last = request.user.last_name
        course = request.POST['course']
        yearlevel = request.POST['yearlevel']
        gender = request.POST['gender']
        phoneNumber = request.POST['phoneNumber']
        email = request.user.email
        guardianNumber = request.POST['guardianNumber']
        guardianName = request.POST['guardianName']
        
        courseInstance = Course.objects.get(pk = course)
        yearInstance = YearLevel.objects.get(pk = yearlevel)
        genderInstance = Gender.objects.get(pk = gender)
        
        studentProfile = Studentprofile(userID = request.user, studentNumber = studentNumber, lastName = last, firstName = first, courseID = courseInstance, yearID = yearInstance, genderID = genderInstance, contactNumber = phoneNumber, emailAddress = email, guardianNumber = guardianNumber, guardianName= guardianName)
        
        studentProfile.save()
        return HttpResponseRedirect(reverse("studentProfile",args=(str(studentNumber),)))
        
    return render(request,"studentForm.html",{
        'courses': Course.objects.all(),
        'yearLevels': YearLevel.objects.all(),
        'gender': Gender.objects.all(),
    })
    
    

def studentProfile(request,studentID):
    studentprof = Studentprofile.objects.get(studentNumber = studentID)
    subjects = Subject.objects.filter(studentProfileID = studentprof)
    if request.method == "POST":
        studentProfileID = studentprof
        subjectCode = request.POST['SubjectCode']
        subjectName = request.POST['subjectName']
        facultyName = request.POST['facultyName']
        units = request.POST['units']
    
        studentSubject = Subject(studentProfileID = studentProfileID,subjectCode = subjectCode,subjectName = subjectName, facultyName= facultyName,units=units)
        
        studentSubject.save()
        studentNumber = studentprof.studentNumber
        return HttpResponseRedirect(reverse("studentProfile",args=(str(studentNumber),)))
    
    return render(request,"studentProfile.html",{
        'studentprof' : studentprof,
        'subjects' : subjects
    })
    
    
def studentSubject(request,studentID,subjectCode):
    profile = Studentprofile.objects.get(studentNumber = studentID)
    subject = Subject.objects.get(studentProfileID=profile,subjectCode=subjectCode)
    return render(request,'studentSubject.html',{
        'subject': subject
    })
    
    
def adminSite(request):
    return render(request, 'admin.html')