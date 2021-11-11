from django.urls import path

from . import views

urlpatterns = [
    path("", views.LineChartsView.as_view(), name="plot"),
    path("data", views.DataApi.as_view(), name="api")
]
