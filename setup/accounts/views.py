from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'accounts/pages/login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class Register(View):
    def get(self, request):
        user_form = UserCreationForm()
        context = {
            'user_form': user_form
        }
        return render(request, 'accounts/pages/register.html', context)

    def post(self, request):
        user_form = UserCreationForm(request.POST)
        context = {
            'user_form': user_form
        }

        if user_form.is_valid():
            user_form.save()
            return redirect('login')

        return render(request, 'accounts/pages/register.html', context)
