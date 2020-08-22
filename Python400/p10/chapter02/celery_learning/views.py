from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from celery import result
from tasks import add
# Create your views here.


def call_add(request):
    # call a task and get task id
    ar = add.delay(2, 3)
    task_id = ar.id

    url = reverse('get_add_result')
    return HttpResponse(f'已经调用任务add，<a href="{url}?task_id={task_id}">查看任务结果</a>。')


def get_add_result(request):
    # get AsyncResult object via task id
    task_id = request.GET['task_id']
    ar = result.AsyncResult(task_id)

    if ar.ready():
        return JsonResponse({'status': ar.state, 'result': ar.get()})
    else:
        return JsonResponse({'status': ar.state, 'result': ''})
