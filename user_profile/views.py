from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib import auth

# Create your views here.
def user_profile_view(request):
    return render(request, 'user_profile.html', {
        'data': "This is user profile content",
    })

class SignUpView(CreateView): #default 'sign in' page, if success, go to login page
    form_class = UserCreationForm
    success_url = "http://127.0.0.1:8000/login/"
    template_name = 'signup_page.html'

def user_login_view(request): #direct to login page
    return render(request, 'login_page.html')

def logout_view(request): #logout and return to main page
    auth.logout(request)
    return HttpResponseRedirect("http://127.0.0.1:8000/main/")

def login(request): #check username and password
    if request.user.is_authenticated:
        return HttpResponseRedirect('http://127.0.0.1:8000/main/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('http://127.0.0.1:8000/main/')
    else:
        return render(request, 'login_page.html', locals())
    
def edit_comment(request): #simply redirect to comment page, todo: pass info for books also
    return render(request, 'comment_page.html')

def add_comment(request): #todo: add comment into database
    return HttpResponseRedirect('http://127.0.0.1:8000/main')

def remove_comment(request): #modify this function to do deletion on specfic comment
    return HttpResponseRedirect('http://127.0.0.1:8000/main/')