
from django.urls import path

from .views import HomeViews

urlpatterns = [
    path('',HomeViews, name="HomeViews"),
]