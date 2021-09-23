from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json

# Single Student- Model object 
def student_detail(request, pk):
    stu = Student.objects.get(id=pk) # complex data
    serializer = StudentSerializer(stu) # converted to python data
    #json_data = JSONRenderer().render(serializer.data)
    json_data = json.dumps(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# All Students - Queryset 
def student_list(request):
    stu = Student.objects.all() # complex data
    serializer = StudentSerializer(stu, many=True) # converted to python data
    #json_data = JSONRenderer().render(serializer.data)
    json_data = json.dumps(serializer.data)
    return HttpResponse(json_data, content_type='application/json')