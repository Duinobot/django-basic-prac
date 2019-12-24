from django.http import HttpResponse
from django.shortcuts import render
from .models import Phone

# Create your views here.
def index(request):
    try:
        phone = Phone(model="i3",storage='32',color='sky',imei="323")
        phone.save()
    except:
        print("cannot insert")
    return render(request, 'appone/index.html')