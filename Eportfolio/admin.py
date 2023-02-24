from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Course)
admin.site.register(YearLevel)
admin.site.register(Gender)
admin.site.register(Studentprofile)
admin.site.register(Subject)



