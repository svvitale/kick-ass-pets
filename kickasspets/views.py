from __future__ import absolute_import, unicode_literals
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from . import tasks
from celery.result import AsyncResult


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
    def get(self, request):
        task = tasks.get_turtle_descriptions.delay()

        return render(request, 'turtles.html', {
            'page': 'turtles',
            'task_id': task.id
        })


class StatusView(View):
    def get(self, request, task_id):

        # Get task by ID
        task_result = AsyncResult(task_id)

        # Check if task is complete
        task_is_complete = task_result.ready()

        if task_is_complete:
            # Retrieve response data
            data = task_result.get()
        else:
            data = None

        return JsonResponse({
            'complete': task_is_complete,
            'data': data
        })
