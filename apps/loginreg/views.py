from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import User, validationManager
import bcrypt
import datetime
# from datetime import datetime


# password = b"super secret password"
#CONTROLLER
#Create your views here.
def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    error = False
    if not validationManager().validateEmail(request, request.POST['email']):
        error = True

    if not validationManager().validateName(request, request.POST['first_name'], request.POST['last_name']):
        error = True
#convert bday
    if not validationManager().validateBirthday(request, request.POST['birthday']):
        error = True

    if not validationManager().validatePassword(request, request.POST['password'], request.POST['password_confirmation']):
        error = True

    if not error:
        hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],birthday=request.POST['birthday'], password=hashed)
        user_row = User.objects.get(email=request.POST['email'], first_name=request.POST['first_name'])
        request.session['user'] = user_row.id
        request.session['name'] = user_row.first_name
        messages.success(request, 'You have successfully been registered!')
        return redirect('/quotes')
    else:
        return redirect('/')

def login(request):
    user = validationManager().validateLogin(request, request.POST['email'], request.POST['password'])
    print user
    if user:
        user_row = User.objects.get(email=request.POST['email'])
        request.session['user'] = user_row.id
        request.session['name'] = user_row.first_name
        print user_row.first_name
        print "name "*10
        return redirect('/quotes')
    else:
        return redirect('/')

def logout(request):
    del request.session['user']
    return redirect('/')
