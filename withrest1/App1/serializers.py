from rest_framework import serializers
from App1.models import Emp

class EmpSerializer(serializers.Serializer):
	def multiples_of_1000(value):
		print("error")
		if value%1000 != 0:
			raise serializers.ValidationError("not a multiples_of_1000")

	def validate_salary(self,value):
		if value < 4999:
			raise serializers.ValidationError("low salary")
		return value

	def validate(self,data):
		name = data.get('name')
		salary = data.get('salary')
		if salary > 50000:
			raise serializers.ValidationError("high salary")
		return data

	def create(self,validated_data):
		return Emp.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.num = validated_data.get('num',instance.num)
		instance.name = validated_data.get('name',instance.name)
		instance.salary = validated_data.get('salary',instance.salary)
		instance.address = validated_data.get('address',instance.address)
		instance.save()
		return instance
	
	num = serializers.IntegerField()
	name = serializers.CharField(max_length=30)
	salary = serializers.FloatField(validators=[multiples_of_1000])
	address = serializers.CharField(max_length=50)