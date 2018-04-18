from django.contrib import admin
from .models import *

myModels= [Company,Applicants]
admin.site.register(myModels)

# Register your models here.

