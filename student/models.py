from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=10)
    grade = models.IntegerField()
    school = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "학생들"

    def __str__(self):
        return self.name
