from django.shortcuts import render

# Create your views here.

def seasons(request):
    return render(request,"seasons/seasons.html") 