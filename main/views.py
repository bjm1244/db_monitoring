import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from main.db_main import show_variable_all


def index(request):
    return render(request, 'main/index.html')


def get_show_variable(request):
    variable_list = show_variable_all()
    return JsonResponse({'data': variable_list}, status=200)


def get_time(request):
    now_time = datetime.datetime.now()
    return JsonResponse({'data': [{
        "variable_idx": 0,
        "variable_name": "current time",
        "value": now_time
    }]}, status=200)

