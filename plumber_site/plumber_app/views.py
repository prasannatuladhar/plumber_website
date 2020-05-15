from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request,'plumber_app/index.html',{})

def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]

        send_mail('I want book a appinment',
        message,
        message_email,
        ['pr_tuladhar@hotmail.com'],
        fail_silently=False,
        )
        return render(request,'plumber_app/contact.html',{'message_name':message_name})    

    else:
        return render(request,'plumber_app/contact.html',{})    
