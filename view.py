import django
from django.http import HttpResponse
from django.shortcuts import render , redirect
from . import settings 
def home_page(response):

    return HttpResponse(settings.BASE_DIR+'<h1>Homepage</h1>')

def data_from_temp(request):
    if 'user' not in request.session:
        return redirect('/login')
    return render(request,'admin/index.html')

def login(request):
    return render(request,'admin/login.html')

def check_auth(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        
        request.session['user'] = username
        return redirect('data_from_temp')