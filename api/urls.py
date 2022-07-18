from django.contrib import admin
from django.urls import include, path

from api.views import ProductView

urlpatterns = [
    path('/product',ProductView.as_view())
]