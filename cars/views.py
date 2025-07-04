from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
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
            cars_search_model = cars.filter(model__icontains=search)
            cars_search_brand = cars.filter(brand__name__icontains=search)
            if cars_search_model.exists():
                return cars_search_model
            elif cars_search_brand.exists():
                return cars_search_brand

        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_cars.html"
    success_url = "/cars/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"
