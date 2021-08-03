from django.urls import path

from todo.views import *
app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('category/new/', CategoryCreateView.as_view(), name='category_new'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
