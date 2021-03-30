from rest_framework import serializers
from core.models import Item
from core.models import UserProfile
class itemSerilzer(serializers.Serializer):
    class Meta :
        model = Item
        fields = '__all__'



class profileSerilzer(serializers.ModelSerializer):
    class Meta :
        model = UserProfile
        field = ({'user'})