
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    tamanho = serializers.IntegerField()
    valor = serializers.FloatField()