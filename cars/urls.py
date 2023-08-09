from django.urls import path

from cars.views import CreateCar, ListCars, DetailCarInfo, EditCar, DeleteCar, CreateNote, ListNote, DetailOrUpdateNote

app_name = 'cars'


urlpatterns = [
    path('car/create', CreateCar.as_view(), name='create-car'),
    path('car/list', ListCars.as_view(), name='list-car'),
    path('car/detail_info/<slug:car>', DetailCarInfo.as_view(), name='detail-car-info'),
    path('car/edit_info/<slug:car>', EditCar.as_view(), name='edit-car-info'),
    path('car/delete_car/<slug:car>', DeleteCar.as_view(), name='delete-car'),
    path('car/create_note/<slug:car>', CreateNote.as_view(), name='create-note-car'),
    path('car/list_note/<slug:car>', ListNote.as_view(), name='list-note'),
    path('car/detail_note/<slug:car_note>', DetailOrUpdateNote.as_view(), name='detail-note'),
    # path('car/edit_note/<slug:car_note>', EditNote.as_view(), name='edit-note'),
]

