from django.shortcuts import render, redirect
from .models import Table
import datetime

def index(request):
    print('iiiiiiiiiii')
    context = {
    "tables":Table.objects.all()
    }
    return render(request,"coursehere/index.html",context)

def process(request):
    time=datetime.datetime.now().strftime("(%Y/%m/%d %-I:%M %p)")
    Table.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect ('/')

def confirmpage(request,id):
    # tables = Table.objects.get(id = id)
    context = {
    "tables" : Table.objects.get(id=id)
    }
    Table.objects.get(id=id)
    print('pringting!')
    return render(request,"coursehere/confirmpage.html", context)

def confirm(request,id):
    x = Table.objects.get(id=id)
    x.delete()
    # print('ccccccccccc')
    return redirect ('/')


#
# def confirm(request):
#     return render(request,"coursehere/confirm.html")

# Create your views here.
