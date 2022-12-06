from django.urls import path
from .import views

urlpatterns=[
path('',views.index),
path('add',views.numadd),
path('show',views.read),
path('del',views.delete),
path('ed',views.update),

]