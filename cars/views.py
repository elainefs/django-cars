from django.views.generic import CreateView, DetailView, ListView

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
