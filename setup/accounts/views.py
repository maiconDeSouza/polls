from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form' : login_form
        }
        return render(request, 'accounts/pages/login.html', context)
