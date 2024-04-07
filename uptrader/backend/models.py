from django.db import models
from django.urls import reverse


class MenuItem(models.Model):

    name = models.CharField(max_length=100, help_text="Название элемента меню")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children',
                               help_text="Родительский элемент меню (пусто для корневых элементов)")
    url = models.CharField(max_length=100, help_text="URL элемента меню")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={'url': self.url})
