from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello Django")
    return render(request,'page/index.html')

def about(request):
    # return HttpResponse("<h1>About Me</h1>")
    name="Rashmikanta"
    students={
        1:{"name":"Rashmi","CGPA":9.1},
        2:{"name":"Jyoti","CGPA":8.0},
        3:{"name":"Sourav","CGPA":9.6}
    }
    context={
        "myname":name,
        "num":21,
        "drinks":['tea','coffee','milk','fruitJuice','cold coffee'],
        "students":students
    }
    return render(request,'page/about.html',context)
