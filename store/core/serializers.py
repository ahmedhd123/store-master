from rest_framework import serializers
from core.models import Item
class itemSerilzer(serializers.Serializer):
    class Meta :
        model = Item
        fields = '__all__'