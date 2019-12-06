from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='sightings'

urlpatterns = [
    path('', views.index, name = "index"),
    path('add/',views.add,name = "add"),
    path('stats/',views.stats,name='stats'),
    path('<Unique_Squirrel_ID>/', views.update, name = "update"),
    path('<Unique_Squirrel_ID>/delete/',views.delete,name = 'delete'),

]
