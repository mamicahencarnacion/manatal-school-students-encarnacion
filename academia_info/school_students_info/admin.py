from django.contrib import admin

from .models import School, Student, StudentDetail

admin.site.register(Student)
admin.site.register(School)
admin.site.register(StudentDetail)
