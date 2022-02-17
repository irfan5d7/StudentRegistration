from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Course)
admin.site.register(models.StudyTerm)
admin.site.register(models.Instructor)
admin.site.register(models.Department)
admin.site.register(models.Registration)
admin.site.register(models.TeachingAssignments)
admin.site.register(models.Student)