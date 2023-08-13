from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from cars.forms.create_note_form import CreateNoteForm
from cars.forms.edit_car_form import EditCarForm
from cars.forms.create_car_form import CreateCarForm
from cars.models import CarPhoto
from cars.models.car_note import CarNote, CarNotePhoto
from cars.models.car import Car
from cars.utils.for_views import delete_car, save_note_about_car, save_car, update_note


class CreateCar(LoginRequiredMixin, View):
    """Создание машины"""

    template_name = "components-cars/create_car.html"

    def get(self, request):
        context = {"title": "Создать машину", "form": CreateCarForm()}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = CreateCarForm(request.POST)
        user = request.user
        file = request.FILES.get("car_photo")

        if form.is_valid():
            cd = form.cleaned_data
            save_car(clean_data=cd, user=user, file=file)
            messages.success(
                request,
                f"Машина {cd['car_brand']} {cd['car_model']} "
                f"с регистрационным номером {cd['reg_number']} добавлена в список",
            )

        return redirect("cars:list-car")


class ListCars(ListView):
    """Список машины"""

    model = Car
    template_name = "car/list_cars.html"
    context_object_name = "my_cars"

    def get_queryset(self):
        user = self.request.user.pk
        return Car.objects.filter(user_id=user, is_deleted=False).prefetch_related(
            "car_photo"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Список машин"
        return context


class DetailCarInfo(DetailView):
    """Детальная информация о машине"""

    template_name = "components-cars/detail_car_info.html"
    model = Car
    slug_url_kwarg = "car"
    context_object_name = "car_object"

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        info = (
            Car.objects.filter(slug=slug)
            .select_related(
                "user",
            )
            .prefetch_related(
                Prefetch("car_photo", queryset=CarPhoto.objects.all()),
                Prefetch(
                    "car_note",
                    queryset=CarNote.objects.filter(car__slug=slug).order_by(
                        "-update_date"
                    ),
                ),
                Prefetch("car_note__car_note_photo"),
            )
        )
        return info

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Детальная информация о машине"
        return context


class EditCar(UpdateView):
    """Редактирование машины"""

    template_name = "components-cars/edit_car_info.html"
    model = Car
    form_class = EditCarForm
    success_url = reverse_lazy("cars:list-car")
    slug_url_kwarg = "car"
    context_object_name = "car_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать информацию о машине"
        return context

    def form_valid(
        self,
        form,
    ):  # TODO Реализовать удаление старой фотографии при создании новой
        self.object = form.save(commit=False)
        if self.request.FILES:
            CarPhoto.objects.update_or_create(
                car=self.object, photo=self.request.FILES["car_photo"]
            )
        self.object.save()
        messages.success(self.request, f"Данные машина успешно изменены")
        return HttpResponseRedirect(self.get_success_url())


class DeleteCar(LoginRequiredMixin, View):
    """Удаление машины (перевод в состояние НЕ АКТИВНЫЙ)"""

    template_name = "components-users/delete_user.html"

    def get(self, request, car):
        delete_car(car)
        temp = car.split("-")
        brand = temp[0]
        model = temp[1]
        reg_number = temp[2].upper()
        messages.success(self.request, f"Машина машина {brand} {model} с {reg_number}")
        return redirect("cars:list-car")


class CreateNote(View):
    """Создание заметки к машине"""

    template_name = "components-cars/create_car_note.html"

    def get(self, request, car=None):
        context = {
            "form": CreateNoteForm(),
            "car_object": get_object_or_404(Car, slug=car),
            "title": "Заметка к машине",
        }
        return render(request, self.template_name, context)

    def post(self, request, car):
        car_obj = get_object_or_404(Car, slug=car)
        form = CreateNoteForm(request.POST)
        photo = request.FILES.getlist("photo")

        if form.is_valid():
            cd = form.cleaned_data
            save_note_about_car(clean_data=cd, car=car_obj, list_of_photos=photo)

        messages.success(self.request, f"Заметка удачно создана")
        return redirect("cars:detail-car-info", car)


class ListNote(View):
    """Список всех заметок к машине"""

    template_name = "components-cars/list_notes.html"

    def get(self, request, car=None):
        car_object = get_object_or_404(
            Car.objects.filter(slug=car)
            .select_related(
                "user",
            )
            .prefetch_related(
                Prefetch("car_photo", queryset=CarPhoto.objects.all()),
                Prefetch(
                    "car_note", queryset=CarNote.objects.all().order_by("-update_date")
                ),
                Prefetch(
                    "car_note__car_note_photo", queryset=CarNotePhoto.objects.all()
                ),
            )
        )

        context = {"car_object": car_object, "title": "Список заметок к машине"}
        return render(request, self.template_name, context)


class DetailOrUpdateNote(
    View
):  # TODO Реализовать удаление фотографии при редактировании
    """Детальная информация заметки к машине и изменение ее"""

    template_name = "components-cars/detail_note.html"

    def get(self, request, car_note=None):
        data = get_object_or_404(
            Car.objects.filter(car_note__slug=car_note)
            .select_related(
                "user",
            )
            .prefetch_related(
                Prefetch("car_note", queryset=CarNote.objects.filter(slug=car_note)),
                Prefetch("car_note__car_note_photo"),
            )
        )
        context = {
            "car_object": data,
            "form": CreateNoteForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, car_note=None):
        slug_for_car = None
        form = CreateNoteForm(request.POST)
        photo = request.FILES.getlist("photo")
        if form.is_valid():
            cd = form.cleaned_data
            slug_for_car = update_note(
                clean_data=cd, list_of_photos=photo, note_slug=car_note
            )

        messages.success(self.request, f"Заметка удачно изменена")
        return redirect("cars:list-note", car=slug_for_car)


class DeleteNote(View):
    """Удаление заметки к машине"""

    def get(self, request, car_note):
        slug = get_object_or_404(Car.objects.filter(car_note__slug=car_note)).slug
        note = get_object_or_404(CarNote, slug=car_note)
        note.delete()
        messages.success(self.request, f"Заявка успешно удалена")
        return redirect("cars:list-note", slug)
