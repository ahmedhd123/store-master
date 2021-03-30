from .models import Item
from .serializers import itemSerilzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAdminUser





@api_view(['GET'])
def itemapi(request):
    all_items = Item.objects.all()
    print(all_items)
    for d in all_items:
        d.title
    
    return Response({'data':all_items})

class ItemView(generics.ListCreateAPIView):
    model = Item
    serializer_class = itemSerilzer
    #permission_classes = [IsAdminUser]