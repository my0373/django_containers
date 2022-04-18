
from django.urls import path

from . import views

# Just add a default index
urlpatterns = [
    path('', views.index, name='index'),
]
