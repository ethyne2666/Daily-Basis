from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context ={
        "variable1":"charan is great guy",
        "variable2":"Kumar is great"
    }
    
    return render(request,'index.html',context)
     #return HttpResponse("this is about page")

def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email,phone=phone,description=description,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request,'contact.html')
