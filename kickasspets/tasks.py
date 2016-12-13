from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests


@shared_task
def get_turtle_descriptions():
    # Get turtle descriptions from the API, deserialize, and return as python list
    api_response = requests.get('http://localhost:8001/turtle-api/descriptions')
    return api_response.json()['turtles']
