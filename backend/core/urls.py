from django.urls import path
from . import views


urlpatterns = [
    path("example/cows-fbv/", views.get_cows_example),
    path("example/barns-fbv/",views.get_barns_example)
]
