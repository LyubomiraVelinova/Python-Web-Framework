from django.shortcuts import render

from charity_for_future.accounts.forms import LoginForm, SignUpForm
from charity_for_future.accounts.models import Login, SignUp


# Create your views here.

def login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        Login.objects.create(
            name=name,
            email=email,
            password=password,
        )
    context = {
        'form': LoginForm()
    }

    return render(request, 'accounts/login-page.html', context)


def register(request):
    if request.method == 'GET':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        form.is_valid()
        first_name = form.cleaned_data['first_name']
        SignUp.objects.create(
            first_name=first_name,
        )
    context = {
        'form': SignUpForm()
    }
    return render(request, 'accounts/signup-page.html', context)
