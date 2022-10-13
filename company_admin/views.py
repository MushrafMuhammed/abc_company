from django.shortcuts import render


def loginfun(request):
    return render(request,'admin_templates/login.html')


def signupfun(request):
    return render(request,'admin_teplates/signup.html')


# Create your views here.
