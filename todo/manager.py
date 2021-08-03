import manager as manager

from todo import models
from .models import *
from django.utils import timezone


class TaskManager(models.Manager):
    def deadlinetask(self):

        return self.filter(time_reached__lt=timezone.now())


class CategoryManager(models.Manager):
    def empty(self):

        return self.filter(tasks__isnull=True)

    def full(self):

        return self.filter(tasks__isnull=False)



