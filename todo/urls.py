from django.urls import path
from . import views

urlpatterns = [
    path('todos',views.todo_list.as_view(),name='todo-list'),
    path('todos/<int:pk>',views.todo_modify.as_view(),name='modify')
    
]