import django
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from . import settings 
def home_page(response):

    return HttpResponse(settings.BASE_DIR+'<h1>Homepage</h1>')

def data_from_temp(request):
    if 'user' not in request.session:
        messages.add_message(request,messages.error,'user is not login')
        return redirect('/login')
    else:
        messages.add_message(request,messages.SUCCESS,' logged in')
    return render(request,'admin/index.html')

def login(request):
    return render(request,'admin/login.html')

def check_auth(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        request.session['user'] = username
        return redirect('/')
def logout(request):
    if 'user' not in request.session:
        return redirect('/login')
    else:
        del request.session['user']
        return redirect('/login')

def form(request):
    return render(request,'admin/form.html')