from django.urls import path
from . import views

urlpatterns = [
    path('', views.archive_view, name='archive_view'),
]
