from django.http import HttpResponse
from django.shortcuts import render
from DocumentsAI.documentsAI import getModel
from DocumentsAI.documentsAI import runQuery
from DocumentsAI.ingest import injest
import os
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
qa=None
def index(request):
    global qa
    qa=getModel()
    return render(request,'index.html')
@require_http_methods(["POST"])
@csrf_exempt
def injest(request):
    injest()
    return JsonResponse({'message': "none"})
@require_http_methods(["POST"])
@csrf_exempt
def askQuestion(request):
    question = request.POST.get('question')
    answer=runQuery(qa,question)
    return JsonResponse({'message': answer})
        