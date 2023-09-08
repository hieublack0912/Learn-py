from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def index(request):
    myname = "Hiếu Black"
    return render(request, "polls/index.html", {"name": myname})