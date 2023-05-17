from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.forms.login_form import LoginForm
from users.forms.registration_form import RegistrationForm


class IndexView(TemplateView):
    # стартовая страница с выбором логирования или регистрации
    template_name = 'index/index.html'
    extra_context = {'title': 'Index'}


class LoginToSite(LoginView):
    """Логирование на сайте (редирект указан в файле settings.py)"""
    template_name = 'index/login.html'
    form_class = LoginForm
    extra_context = {'title': 'Вход'}


class RegistrationOnSite(View):
    """Регистрация на сайте"""
    template_name = 'index/registration.html'

    def get(self, request):
        context = {
            'title': 'Регистрация',
            'reg_form': RegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'title': 'Регистрация',
            'reg_form': form
        }
        return render(request, self.template_name, context)
