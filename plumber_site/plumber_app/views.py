from django.shortcuts import render
from .models import AppointmentInfo
from django.core.mail import send_mail
from .forms import AppointmentInfoForm

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

def about(request):
    return render(request,'plumber_app/about.html',{})


def blogdetails(request):
    return render(request,'plumber_app/blog-details.html',{})


def blog(request):
    return render(request,'plumber_app/blog.html',{})


def pricing(request):
    return render(request,'plumber_app/pricing.html',{})


def service(request):
    return render(request,'plumber_app/service.html',{})

def appointment(request):
    if request.method == "POST":
        form = AppointmentInfoForm(request.POST or None)
        your_name = request.POST["your-name"]
        your_phone = request.POST["your-phone"]
        your_email = request.POST["your-email"]
        your_address = request.POST["your-address"]
        your_time = request.POST["your-time"]
        # your_date = request.POST["your-date"]
        your_message = request.POST["your-message"]
        if form.is_valid():
            form.save()
            send_mail('I want to book a appointment',
            your_message,
            your_email,
            ['prasanna.pmt@gmail.com'],
            fail_silently=False,
            )
            return render(request,'plumber_app/appointment.html',{'your_message':your_message})
        else:    
            return render(request,'plumber_app/index.html',{})    

    else:
        return render(request,'plumber_app/index.html',{})    