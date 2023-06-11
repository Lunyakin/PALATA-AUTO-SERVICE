from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView

from cars.forms.edit_car_form import EditCarForm
from cars.forms.create_car_form import CreateCarForm
from cars.models import Cars
from cars.utils.for_views import create_slug


class CreateCar(CreateView):
    """ Создание машины """
    model = Cars
    template_name = 'components-cars/create_car.html'
    form_class = CreateCarForm
    success_url = reverse_lazy('cars:list-car')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать машину'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        car_brand = form.cleaned_data['car_brand']
        car_model = form.cleaned_data['car_model']
        reg_number = form.cleaned_data['reg_number']
        form.instance.slug = create_slug(car_brand=car_brand, car_model=car_model, reg_number=reg_number)

        messages.success(
            self.request, f"Машина {car_brand} {car_model} с регистрационным номером {reg_number} добавлена в список"
        )

        return super().form_valid(form)


class ListCars(ListView):
    """ Список машины """
    model = Cars
    template_name = 'components-cars/list_cars.html'

    def get_queryset(self):
        user = self.request.user.pk
        object_list = Cars.objects.filter(user_id=user)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список машин'
        return context


class DetailCarInfo(DetailView):
    """ Детальная информация о машине """
    template_name = 'components-cars/detail_info.html'
    model = Cars
    slug_url_kwarg = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Детальная информация о машине'
        return context


class EditCar(UpdateView):
    """ Редактирование машины """
    template_name = 'components-cars/edit_car_info.html'
    model = Cars
    form_class = EditCarForm
    success_url = reverse_lazy('cars:list-car')
    slug_url_kwarg = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать информацию о машине'
        return context
