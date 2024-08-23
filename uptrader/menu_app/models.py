from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    path = models.CharField(max_length=200, default="", unique=True)

    def __str__(self):
        return f"{self.label} ({self.menu})"
