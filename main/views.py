import datetime
import logging

from django.http import JsonResponse
from django.shortcuts import render
from main.db_main import show_variable_all

logger = logging.getLogger('py_log')


def index(request):
    return render(request, 'main/index.html')


def get_show_variable(request):
    if request.method == 'POST':
        variable_list = show_variable_all()
        logger.info("system variable list : {}".format(variable_list))
        return JsonResponse({'data': variable_list}, status=200)


def get_time(request):
    if request.method == 'POST':
        now_time = datetime.datetime.now()
        now_date_list = [{
            "variable_idx": 0,
            "variable_name": "current time",
            "value": now_time
        }]
        logger.info("now date list : {}".format(now_date_list))
        return JsonResponse({'data': now_date_list}, status=200)
