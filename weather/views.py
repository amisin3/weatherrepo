from django.shortcuts import render
from django.http import HttpResponse
import urllib
import json
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4c20e78422db258277de544b28e81eac'
    
    if request.method=="POST":
        form = CityForm(request.POST)
        form.save()


    form = CityForm()    

    cities = City.objects.all()
    
    weather_report = []
    for city in cities:
        u_get = urllib.request.urlopen(url.format(city)).read()
        output = json.loads(u_get)
        city_weather = {
            'city_name': output['name'],
            'temperature': output['main']['temp'],
            'description': output['weather'][0]['description'],
            'logo': output['weather'][0]['icon']

        }

        weather_report.append(city_weather)

    return HttpResponse(render(request, "weather/index.html", {'weather_report': weather_report, 'form': form}))

