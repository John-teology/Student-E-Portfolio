from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.


class User(AbstractUser):
    pass


class Course(models.Model):
    course = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course}"

class YearLevel(models.Model):
    yearLevel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.yearLevel}"
    
class Gender(models.Model):
    gender = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.gender}"
    
class Studentprofile(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE, related_name= 'studentProfile' )
    studentNumber = models.CharField(max_length=25, blank=True)
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    courseID = models.ForeignKey(Course, on_delete=CASCADE ,related_name='studentCourse' )
    yearID = models.ForeignKey(YearLevel, on_delete=CASCADE,  related_name= 'studentYearLevel' )
    genderID = models.ForeignKey(Gender, on_delete=CASCADE,  related_name= 'studentGender' )
    contactNumber = models.IntegerField()
    emailAddress = models.CharField(max_length=25)
    guardianNumber = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.studentNumber} : {self.lastName}, {self.firstName}"
    

    