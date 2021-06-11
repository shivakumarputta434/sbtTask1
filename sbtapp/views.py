from django.shortcuts import render,HttpResponse
from .models import Employee

# Create your views here.

#This is tesing function
def home(request):
    emp=Employee.objects.get(id=1)
    name=emp.firstName
    print(name)
    return HttpResponse(name)


#Employee Api's Get, Post, Update and Delete

from rest_framework.views import APIView
from .serializer import EmpSerializer
from  rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404

class EmpData(APIView):
    def get(self,request,*args,**kwargs):
        if kwargs.get('id'):
            id=kwargs.get('id')
            try:
                singleEmpdata=Employee.objects.get(id=id)
                saved_data=EmpSerializer(singleEmpdata)
                return Response(saved_data.data)
            except:
                return Response({'msg':'data doesnot exist'})
        data=Employee.objects.all()
        saved_data=EmpSerializer(data,many=True)
        return Response(saved_data.data)

    def post(self,request,*args,**kwargs):
        empdata=EmpSerializer(data=request.data)
        if empdata.is_valid():
            empdata.save()
            return Response(empdata.data,status=status.HTTP_201_CREATED)
        else:
            return Response(empdata.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        EditEmp=get_object_or_404(Employee.objects.all(),id=id)
        empdata=EmpSerializer(instance=EditEmp,data=request.data,partial=True)
        if empdata.is_valid(raise_exception=True):
            empdata.save()
        return Response({'msg':'data updated succsessfully'})

    def delete(self,request,id):
            singleEmpdata=get_object_or_404(Employee.objects.all(),id=id)
            singleEmpdata.delete()
            return Response({'msg':'data deleted successfully'})



