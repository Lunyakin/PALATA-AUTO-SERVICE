from django.urls import path

from cars.views import CreateCar, ListCars, DetailCarInfo, EditCar, DeleteCar

app_name = 'cars'


urlpatterns = [
    path('car/create', CreateCar.as_view(), name='create-car'),
    path('car/list', ListCars.as_view(), name='list-car'),
    path('car/detail_info/<slug:car>', DetailCarInfo.as_view(), name='detail-car-info'),
    path('car/edit_info/<slug:car>', EditCar.as_view(), name='edit-car-info'),
    path('car/delete_car/<slug:car>', DeleteCar.as_view(), name='delete-car'),
]

