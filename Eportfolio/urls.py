from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("studentform/",views.demographicForm, name="demographicForm"),
    path("studentprofile/<str:studentID>",views.studentProfile,name="studentProfile"),
     path("studentprofile/<str:studentID>/<str:subjectCode>",views.studentSubject,name="studentSubject"),
    path("siteadmin",views.adminSite,name="adminsite")
    
    
]