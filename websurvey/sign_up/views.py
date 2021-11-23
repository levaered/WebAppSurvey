from django.shortcuts import render
def index(request):
    return render(request, 'main/index.html')
def login(request):
    return render(request, 'sign_up/login.html')
def sign(request):
    return render(request, 'sign_up/sign.html')

