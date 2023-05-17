from django.urls import path

from users.views import index

urlpatterns = [
    path('', index, name='index'),
]
