from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
from django.core.mail import send_mail



# Create your views here.
def index(request):
    return render(request,'base/index.html')

def about(request):
    return render(request,'base/about.html')

def post(request):
    return render(request,'base/post.html')

def contact(request):
   
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        new_user = User(name=name, email=email, phone=phone, message=message)
        new_user.save()

        send_mail(
            'Message From'+ name,
            email,
            message,
            ['tejasnirmal11@gmail.com'],
        )
        return HttpResponse("FORM SUBMISSION IS SUCCESSFUL and YOUR MAIL IS RECEIVED")



    return render(request,'base/contact.html')






