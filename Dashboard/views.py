from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .tasks import my_task


def index(request):
    result = my_task.delay(10)
    return render(request, 'index.html', {'task_id' : result.task_id})
