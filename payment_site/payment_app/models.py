from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    description = models.TextField(max_length=500, verbose_name='Описание товара')
    price = models.IntegerField(default=0, verbose_name='Цена товара') # в копейках

    def __str__(self):
        return self.name

    def show_price(self):
        return "{0:.2f}".format(self.price / 100)
