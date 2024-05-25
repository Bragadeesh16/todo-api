from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_list.as_view(),name='todo-list'),
    path('update/<int:pk>',views.todo_modify.as_view(),name='modify')
    
]