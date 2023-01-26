from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("studentform/",views.demographicForm, name="demographicForm"),
    path("home/",views.mainpage,name="home")
    
]