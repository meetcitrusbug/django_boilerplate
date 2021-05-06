from cart.models import Cart
from rest_framework.serializers import ModelSerializer

class AddItemsSerializer(ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ('user', 'product', 'quantity')