from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path("test3/hello", views.say_hello)
]