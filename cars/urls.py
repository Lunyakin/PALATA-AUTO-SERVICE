from django.urls import path

from cars.views import CreateCar, ListCars
app_name = 'cars'


urlpatterns = [
    path('car/create', CreateCar.as_view(), name='create-car'),
    path('car/list', ListCars.as_view(), name='list-car'),
]

