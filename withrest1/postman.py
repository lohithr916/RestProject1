import requests
import json
BASE_URL = 'http://127.0.0.1:800/'
ENDPOINT = 'emp/'

def get_resource(id=None):
	data ={}
	if id is not None:
		data = {'id':id}
		response = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
		print(response.json,end=" ")
		print(response.status_code)

def create_resource():
	new_emp = {'num':1,'name':'Jo','salary':9000,'address':'NY'}
	response = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
	print(response.json,end=" ")
	print(response.status_code)

def update_resource(id):
	update_emp = {'name':'Seetha','salary':9801,'address':'LV'}
	response = requests.put(BASE_URL+ENDPOINT,data=json.dumps(update_emp))
	print(response.json,end=" ")
	print(response.status_code)

def delete_resource(id):
	data = {'id':id}
	response = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
	print(response.json,end=" ")
	print(response.status_code)