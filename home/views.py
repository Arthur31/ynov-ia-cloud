from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
@login_required(login_url='register')
def home(request):
    return render(request, 'home/index.html', locals())


def login_route(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            print(' login and redirect')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            # No backend authenticated the credentials
            print('wrong login')
            errors = []
            errors.append('invalid username or password')
            return render(request, 'home/login.html',{
                'errors' : errors
            })

    else:
        return render(request, 'home/login.html')

def logout_route(request):
     logout(request)
     return redirect('login')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend' )
            return redirect('/')
        else:
            return render(request, 'home/register.html', {
                'form' : form
            })
    else:
        form = SignUpForm()
        return render(request, 'home/register.html', {
            'form' : form
        })