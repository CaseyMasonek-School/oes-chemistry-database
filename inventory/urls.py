from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:item_id>',views.show, name="show"),
    path("filtered",views.filtered)
]

