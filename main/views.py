from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    if request.method =='GET':
        return render(request, 'main/index.html')
    elif request.is_ajax():
        data_entered = request.POST.get('text', None)
        if data_entered:
            response = {
                'msg': data_entered
            }
            return JsonResponse(response)
        else:
            response = {
                'msg': ""
            }
            return JsonResponse(response)

def workspace(request):
    if request.method =='GET':
        return render(request, 'main/editPage.html')
    elif request.is_ajax():
        data_entered = request.POST.get('text', None)
        if data_entered:
            response = {
                'msg': data_entered
            }
            return JsonResponse(response)
        else:
            response = {
                'msg': ""
            }
            return JsonResponse(response)