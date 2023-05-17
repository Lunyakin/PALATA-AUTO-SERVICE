from django.urls import path

from users.views import IndexView, LoginToSite, RegistrationOnSite

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginToSite.as_view(), name='login'),
    path('registration', RegistrationOnSite.as_view(), name='registration')

]
