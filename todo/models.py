from django.db import models
from django.urls import reverse
from .manager import *
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    objects = CategoryManager()

    def get_absolute_url(self):
        return reverse('todo:category_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    class meta:
        pass

    PRIORITY = [('Top', 'Top'), ('medium', 'Medium'), ('Down', 'Down')]
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    category = models.ManyToManyField(Category, blank=True, related_name='tasks')
    priority = models.CharField('priority', max_length=10, choices=PRIORITY)
    time_reached = models.DateTimeField('Times hit task')
    objects = TaskManager()

    def get_absolute_url(self):
        return reverse('todo:task_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.title} and {self.category}"




