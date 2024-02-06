from django.contrib import admin
from students.models import Students,CustomUser

admin.site.register(Students)
admin.site.register(CustomUser)