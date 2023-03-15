from django.shortcuts import render
from rest_framework import generics

from api.models import DataTable
from api.serializers import ApiSerialier

class ListaInadimplentes(generics.ListAPIView):
    queryset = DataTable.objects.all()
    serializer_class = ApiSerialier
