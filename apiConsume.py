import requests

send1 = {
     'name': 'You',
     'email': 'you@hot.com',
     'phone':  '04127562013'
}

r = requests.post('http://127.0.0.1:8000/api/reserves/date-create/', data=send1)


