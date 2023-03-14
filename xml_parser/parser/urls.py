from django.urls import path
from . import views

urlpatterns = [
        path('contattaci', views.executeParse, name='contattaci')
]

