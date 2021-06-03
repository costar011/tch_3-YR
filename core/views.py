from django.shortcuts import render
from student import models as stu_models


def homeRender(request):

    stu_list = stu_models.StudentModel.objects.all()

    return render(request, "screens/home.html", context={"stu_list": stu_list})
