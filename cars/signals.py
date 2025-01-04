from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum("value"))["total_value"]
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, created, **kwargs):
    if not instance.bio:
        instance.bio = "Este carro combina estilo, conforto e desempenho, sendo uma ótima escolha para quem busca qualidade e confiabilidade. Com um design marcante e um interior que oferece conforto, ele é ideal tanto para o uso diário quanto para momentos especiais. Cada detalhe foi pensado para garantir uma condução prazerosa, segura e eficiente."


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, created, **kwargs):
    car_inventory_update()
