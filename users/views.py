from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView

from users.forms.delete_user_form import DeleteUserForm
from users.forms.edit_user_form import EditUserForm
from users.forms.login_form import LoginForm
from users.forms.registration_form import RegistrationForm
from users.utils.for_views import delete_user

User = get_user_model()


class IndexView(TemplateView):
    """ Стартовая страница с выбором логирования или регистрации """
    template_name = 'users/index.html'
    extra_context = {'title': 'Index'}


class LoginToSite(LoginView):
    """Логирование на сайте (редирект указан в файле settings.py)"""
    template_name = 'users/login.html'
    form_class = LoginForm
    extra_context = {'title': 'Вход'}


class LogOut(LogoutView):
    extra_context = {'title': 'Выход'}


class RegistrationOnSite(View):
    """Регистрация на сайте"""
    template_name = 'users/registration.html'

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
            return redirect('users:home')
        context = {
            'title': 'Регистрация',
            'reg_form': form
        }
        return render(request, self.template_name, context)


class HomeView(TemplateView):
    """ Стартовая страница с выбором логирования или регистрации """
    template_name = 'users/home.html'
    extra_context = {
        'title': 'Домашняя',
        'topic': 'Основной отчет'
    }


class ProfileView(LoginRequiredMixin, TemplateView):
    """Отображение информации об пользователе"""
    template_name = 'users/user.html'

    def get_context_data(self, **kwargs) -> dict:
        context = {
            'title': 'Страница профиля',
            'topic': 'Профиль'
        }
        return context


class EditProfile(LoginRequiredMixin, UpdateView):
    """Редактирование информации об пользователе"""
    model = User
    template_name = 'components-users/edit_profile.html'
    form_class = EditUserForm
    success_url = reverse_lazy('users:profile')
    success_message = "User updated"

    def get_object(slef):
        return slef.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        context['topic'] = 'Редактирование профиля'
        return context


class DeleteProfile(LoginRequiredMixin, View):
    """Удаление аккаунта пользователя (перевод в состояние НЕ АКТИВНЫЙ)"""
    template_name = 'components-users/delete_user.html'

    def get(self, request):
        context = {
            'title': 'Удаление аккаунта',
            'topic': 'Удаление аккаунта',
            'del_form': DeleteUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            delete_user(request.user)
            return redirect('users:registration')
        context = {'del_form': form}
        return render(request, self.template_name, context=context)


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    """Изменение пароля пользователя"""
    template_name = 'components-users/change_password.html'
    success_url = reverse_lazy("users:profile")
