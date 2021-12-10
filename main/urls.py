from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_variable_all/', views.get_show_variable, name='variable_all'),
]