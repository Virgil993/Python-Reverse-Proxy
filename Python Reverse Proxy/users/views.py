from datetime import datetime
import http
from time import time
from django.http import HttpResponse
import urllib
import json
from . import models


# Create your views here.

def users(request):
    req = models.Requests()
    req.header = str(request.headers)
    req.time = str(datetime.now())
    req.save()
    current_url = request.path_info
    number = ''
    for i in range(len(current_url)):
        if current_url[i] >='0' and current_url[i]<='9':
            number=number+current_url[i]
    next_url = 'https://jsonplaceholder.typicode.com/users/'+number
    get_response= urllib.request.urlopen(next_url)
    data = json.loads(get_response.read())
    data["foo"]="bar"
    response = HttpResponse(json.dumps(data), headers = {'Content-Type':'application/json'})
    resp = models.Responses()
    resp.header = str(response.headers)
    resp.time = str(datetime.now())
    resp.body = str(response.content)
    resp.save()
    return response