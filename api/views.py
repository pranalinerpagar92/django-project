from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer, EmployeeSeraializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


#companies/{company_id}/employee
    @action(detail=True, methods=['get'])
    def employee(self, request, pk=None):
        try:
            company = Company.objects.get(pk= pk)
            emps = Employee.objects.filter(company=company)
            emps_serialzer = EmployeeSeraializer(emps, many=True,context={'request': request})
            return Response(emps_serialzer.data)
        except Exception as e:
            print(e)
            return Response({'message': 'Company might not Exists !!'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSeraializer

