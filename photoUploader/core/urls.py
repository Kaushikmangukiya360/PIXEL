from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', view=views.index),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]
