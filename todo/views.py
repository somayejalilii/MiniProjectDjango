from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Task, Category


from django.shortcuts import render

# Create your views here.
class TaskListView(ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = 'Task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'Task_Detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'Task_Create.html'
    fields = ('title', 'description', 'priority', 'category', 'time_reached')


class CategoryListView(ListView):
    model = Category
    template_name = 'Category_list.html'

    def get_queryset(self):
        obj = {'queryset': Category.objects.full(),
               'queryset1':  Category.objects.empty()
         }
        return obj

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'Category_Detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'Category_Create.html'
    fields = ('name',)

