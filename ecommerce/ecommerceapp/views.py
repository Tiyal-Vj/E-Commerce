from django.shortcuts import render

def index(request):
    return render(request,"index.html")# Create your views here.

def contact(request):
    return render(request,"contact.html")# Create your views here.
def about(request):
    return render(request,"about.html")# Create your views here.

