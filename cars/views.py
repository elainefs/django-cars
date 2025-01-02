from django.shortcuts import redirect, render
from django.views import View

from .forms import CarModelForm
from .models import Car


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by("model")
        search = request.GET.get("search")

        if search:
            cars = cars.filter(model__icontains=search)

        return render(request, "cars.html", {"cars": cars})


class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, "new_cars.html", {"new_car_form": new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
        return render(request, "new_cars.html", {"new_car_form": new_car_form})
