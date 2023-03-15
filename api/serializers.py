from rest_framework import serializers

from api.models import DataTable


class ApiSerialier(serializers.ModelSerializer):

    class Meta:
        model = DataTable
        fields = '__all__'
