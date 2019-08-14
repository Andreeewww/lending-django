from django.urls import path
from .views import lending

urlpatterns = [
    path('', lending),
]