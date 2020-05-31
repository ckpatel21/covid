from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"India"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "708f63e471mshcc645af192986c4p1fe189jsn425c76ed3a9d"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']

    d = data[0]

    print(d)

    context = {
        'all' : d['cases']['total'],
        'recovered' : d['cases']['recovered'],
        'deaths' : d['deaths']['total'],
        'new' : d['cases']['new'],
        'critical' : d['cases']['critical']

    }

    return render(request,'index.html',context)

