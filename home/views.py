from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact # TO use Contact Class
from django.contrib import messages #For alert purpose
# Create your views here.
def index(request):
    context = {
        'variable':"this is sent",
        'variable2':"this is also sent"
    }
    return render(request , "index.html", context)

def about(request):
    return render(request , "about.html")

    # return HttpResponse("this is about page")

def services(request):
    return render(request , "services.html")
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email,phone = phone , desc= desc  , date = datetime.today())
        contact.save()
        messages.success(request, 'Your messages has been sent')
    return render(request , "contact.html")
    # return HttpResponse("this is contact page")