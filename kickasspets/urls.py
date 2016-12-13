"""kickasspets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from kickasspets.views import DogView, CatView, TurtleView, StatusView


urlpatterns = [
    url(r'^$', DogView.as_view()),
    url(r'^dogs$', DogView.as_view()),
    url(r'^cats$', CatView.as_view()),
    url(r'^turtles$', TurtleView.as_view()),

    url(r'^status/(?P<task_id>[a-f\d\-]+)', StatusView.as_view())
]
