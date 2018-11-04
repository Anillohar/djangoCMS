from django.contrib.auth import authenticate
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'html/dashboard.html')
            else:
                return render(request, 'html/dashboard.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        user = get_user_model()
        if email is not None:
            user.objects.filter(email=email)
            send_mail(
                'Django email',
                'Sir mail aaya?.',
                'anillohar03@gmail.com',
                ['malu.ram@owebest.com'],
                fail_silently=False,
            )
            return render(request , 'registration/login.html' , {'error_message' : 'Mail sent'})
        else:
            return render(request , 'registration/forgot_password.html' , {'error_message' : 'email id doesnot exist'})
    return render(request , 'registration/forgot_password.html')
