from rest_framework import serializers
from .models import Employee

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.firstName=validated_data.get('firstName',instance.firstName)
        instance.email = validated_data.get('email', instance.email)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
