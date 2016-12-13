from django.shortcuts import render
from django.views import View
import requests


class DogView(View):
    def get(self, request):
        return render(request, 'dogs.html', {
            'page': 'dogs'
        })


class CatView(View):
    def get(self, request):
        return render(request, 'cats.html', {
            'page': 'cats'
        })


class TurtleView(View):
    def get_turtle_descriptions(self):
        # Get turtle descriptions from the API, deserialize, and return as python list
        api_response = requests.get('http://localhost:8001/turtle-api/descriptions')
        return api_response.json()['turtles']

    def get(self, request):
        return render(request, 'turtles.html', {
            'page': 'turtles',
            'data': self.get_turtle_descriptions()
        })
