from django.urls import path
from .views import *

urlpatterns = [
    path('home/', view=home, name="home"),
    path('', view=home, name="home"),
]