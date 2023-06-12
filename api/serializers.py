from rest_framework import serializers
from api.models import Company,Employee


#creating company serializer

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'


#creating employee serializer

class EmployeeSeraializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'

