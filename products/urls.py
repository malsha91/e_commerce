from django.urls import path

from . import views

urlpatterns = [
    path("new2/", views.index, name="index"),
]