import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login ,logout
from .models import chart_user

def register(request):
    return render(request,"signup.html")

def singup(request):
    user_exist=True
    if request.method=='POST':
        first_name=request.POST.get('name')
        email=request.POST.get('email_register')
        password=request.POST.get('pass_register')
        print(first_name,email,password)
        user = User.objects.create_user(first_name = request.POST.get('name'), 
                                        # last_name = request.POST.get('mob'), 
                                        username = request.POST.get('email_register'),
                                        password=request.POST.get('pass_register'))
        # chart_user_profile=chart_user(name_user=user,dob="01/01/2022",state="delhi",email=False)
        login(request, user)

        user.save()
        # chart_user_profile.save()
    return redirect("/")

def signin(request):
    if request.method=='POST':
        username=request.POST.get('email').lower()
        password=request.POST.get('pass')
        user = authenticate(request, username = request.POST.get('email').lower(), password = request.POST.get('pass'))
        if user is not None :
            login(request, user)
            print(user)
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')