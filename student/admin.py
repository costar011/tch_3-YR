from django.contrib import admin
from . import models


@admin.register(models.StudentModel)
class StudentAdmin(admin.ModelAdmin):
    pass
