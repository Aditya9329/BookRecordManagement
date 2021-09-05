from django.shortcuts import render
import requests
from api import models
from django.http import HttpResponse
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf  import csrf_exempt
# Create your views here.
#model object one by one


def student_detail(request):
    #working model object
    s=models.Student.objects.get(id=1)
    print(s)
    #seraialzier object
    sr=StudentSerializers(s)#passing model object data to serializer
    print(sr)
    json_data=JSONRenderer().render(sr.data)#finally data will be in JSON format
    return HttpResponse(json_data,content_type='application/json')

#working with queryset serializers
def student_list(request):
    s=models.Student.objects.all()
    print(s)
    #seraialzier object
    sr=StudentSerializers(s,many=True)
    print(sr)
    json_data=JSONRenderer().render(sr.data)
                                    #keyword argument
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def NewStudent(request):
    if request.method=='POST':
        json_data=request.body
        #converting the json daat to stream
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        #convertingt the python data to complex data
        sr=StudentSerializers(data=py_data)
        #validate
        if sr.is_valid():
            sr.save()
            res={'msg':'data sucessfully inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(sr.errors)
        return HttpResponse(json_data,content_type='application/json')

