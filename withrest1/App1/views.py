from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from App1.serializers import EmpSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from App1.models import Emp
import io

@method_decorator(csrf_exempt,name='dispatch')
class EmpView(View):
	def get(self,request,*args,**kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data) #converting json data into python data ie dict
		pydata = JSONParser().parse(stream)
		id = pydata.get('id',None)
		if id is not None:	
			emp = Emp.objects.get(id=id)
			print(emp)
			if emp is None:
				msg = {'msg':'record not found'}
				json_data = JSONRenderer.render(msg)
				return HttpResponse(json_data,content_type='application/json',status=500)
			serializer = EmpSerializer(emp)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data,content_type='application/json',status=200)		
		qs = Emp.objects.all()
		serializer = EmpSerializer(qs,many=True)
		json_data = JSONRenderer().render(serializer.data)
		return HttpResponse(json_data,content_type='application/json',status=200)

	def post(self,request,*args,**kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		serializer = EmpSerializer(data=pydata)
		if serializer.is_valid():
			serializer.save() #internally calls create()
			msg = {'msg':'created'}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json',status=201)
		else:
			msg = {'msg':'error'}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json',status=400)

	def put(self,request,*args,**kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		empid = pydata.get('id')
		emp = Emp.objects.get(id=empid)
		serializer = EmpSerializer(emp,data=pydata,partial=True)#update emp with provided data
		if serializer.is_valid():
			serializer.save() #internally calls update()
			msg = {'msg':'updated'}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json',status=201)
		else:
			msg = {'msg':'error'}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json',status=400)
		#by default put() accept complete data not partial data

	def delete(self,request,*args,**kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		empid = pydata.get('id')
		emp = Emp.objects.get(id=empid)
		emp.delete()
		msg = {'msg':'deleted'}
		json_data = JSONRenderer().render(msg)
		return HttpResponse(json_data,content_type='application/json',status=200)