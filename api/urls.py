from django.urls import path

from .views import ListaInadimplentes

urlpatterns = [
    path('v1/', ListaInadimplentes.as_view()),
    ]