from django.shortcuts import render

from PyWeb.models import UserInfo


def login(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')


def register(request):
    account = request.POST.get("account", None)
    password = request.POST.get("password", None)
    print(account, password)
    UserInfo.objects.create(account=account, password=password)
    return render(request, 'register.html')
