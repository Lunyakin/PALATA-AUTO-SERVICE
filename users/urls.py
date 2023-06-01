from django.urls import path

from users.views import IndexView, LoginToSite, RegistrationOnSite, HomeView, LogOut, ProfileView, EditProfile, \
    DeleteProfile

app_name = 'users'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginToSite.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('registration', RegistrationOnSite.as_view(), name='registration'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('edit-profile', EditProfile.as_view(), name='edit-profile'),
    path('delete', DeleteProfile.as_view(), name='delete-profile'),
    path('home', HomeView.as_view(), name='home')

]
