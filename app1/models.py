from django.db import models
from django.utils.translation import ugettext_lazy as _


class Shop(models.Model):
    name = models.CharField(verbose_name=_('Название магазина'), max_length=255, blank=False)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    street = models.ForeignKey("Street", on_delete=models.CASCADE)


class City(models.Model):
    city = models.CharField(verbose_name=_('Название города'), max_length=255, blank=False)


class Street(models.Model):
    street = models.CharField(verbose_name=_('Название улицы'), max_length=255, blank=False)
    city = models.ForeignKey("City", on_delete=models.CASCADE)

