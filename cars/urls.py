from django.urls import path

app_name = 'cars'


urlpatterns = [
    path('car/create', CreateCar.as_view(), name='create-car'),
]

