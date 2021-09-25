import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id }
    headers = {'Content-Type': 'application/json'}        
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
    
#get_data(5)  


def post_data():
    data = {
        'name': 'Kante',
        'roll': 110,
        'city': 'Chelsea'
    }   
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

#post_data()


def update_data():
    data = {
        'id': 6,
        'name': 'Azpi',
    }   
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)   
    
#update_data()     


def delete_data():
    data = { 'id': 6 }    
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
    
delete_data()        
    