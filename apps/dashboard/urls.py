from django.urls import path
# from .views import *
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.show, name='show'),
    path('insert/', views.insert, name='insert')
]