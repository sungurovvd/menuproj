from django.db import models


class Item(models.Model):
    menu_name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    url = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null= True)

    def __str__(self):
        return f'{self.menu_name}: {self.text}'

