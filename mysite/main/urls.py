from django.urls import path
from . import views 

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("v1/", views.v1, name="v1"),
]