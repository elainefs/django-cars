from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CarModelForm
from .models import Car


class CarsView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")

        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_cars.html"
    success_url = "/cars/"


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})

