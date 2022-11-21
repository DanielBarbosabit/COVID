from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('indextest', views.index, name='index'),
    path('indexstart', views.index, name='index'),
    path('ind', views.index, name='index'),
    path('inde', views.index, name='index'),
    path('in', views.index, name='index'),
    path('newpath', views.index, name='index'),
    path('path', views.index, name='index'),
]
