from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lending (request):
    return render(request, 'block/test.html')