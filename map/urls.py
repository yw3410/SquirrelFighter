from django.urls import path

from . import views

urlpatterns = [
    path('', views.squirrels_map, name='squirrels_map'),
]
