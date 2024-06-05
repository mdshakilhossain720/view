from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Student
from.serlilazers import Studentserilazers



# Create your views here.
@api_view(['GET','POST','DELETE','PUT'])
def studentapi(request):
    if request.method == 'GET':
        id=request.data.get(id)
        if id is not None:
            stu=Student.objects.get(id=id)
            serlizar=Studentserilazers(stu)
            return Response(serlizar.data)
        stu=Student.objects.all()
        serlizar=Studentserilazers(stu,many=True)
        return Response(serlizar.data)
    

    if request.method == 'POST':
        serlizar=Studentserilazers(data=request.data)
        if serlizar.is_valid():
            serlizar.save()
            return Response({'msg':'Data Created'})
        return Response(serlizar.errors)
    
    if request.method == 'PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serlizar=Studentserilazers(stu,data=request.data,partial=True)
        if serlizar.is_valid():
            serlizar.save()
            return Response({'msg':'Update data'})
        return Response(serlizar.errors)
    


        
             

            
        





















# @api_view(['GET'])
# def hello_world(request):
#     return HttpResponse({'msg':'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':

#       return HttpResponse({'msg':'Hello World','data':request})
