from django.shortcuts import render , HttpResponse
from datetime import datetime
from Home.models import Contact
# Create your views here.
def index(request):
    context = {
      
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page.")

def about(request):
    context = {
        # 'variable' : "this is sent"
    }
    return render(request, 'about.html', context)
    # return HttpResponse("This is about page.")

def services(request):
    context = {


        # 'variable' : "this is sent"
    }
    return render(request, 'services.html', context)
   #  return HttpResponse("this is service page")

def contact(request):
    context = {
        # 'variable' : "this is sent"
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
       # subject = request.POST.get('Subject')
       # message = request.POST.get('Message')
        contact = Contact(name= name , email= email  , date = datetime.today())
        contact.save()
    return render(request, 'contact.html', context)
  # return HttpResponse("This is contact page.")