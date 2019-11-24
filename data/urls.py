from django.urls import path

from . import views

app_name = "data"
urlpatterns = [
    path("", views.index, name="index"),
    path("nqrw", views.nqrw_feed, name="nqrw_feed"),
]
