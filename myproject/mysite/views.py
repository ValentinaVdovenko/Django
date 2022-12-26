from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request - объект класса HttpResponse
def index(request):
    return render(request,'mysite/index.html')

def about(request):
    return render(request,'mysite/about.html')    
