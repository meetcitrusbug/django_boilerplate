from rest_framework import serializers
from order.models import UserCard

class CardListSerializer(serializers.ModelSerializer):
    
    last4 = serializers.SerializerMethodField('get_last4')
    class Meta:
        model = UserCard
        fields = ['id', 'brand', 'last4', 'is_default', 'name']
        
    def get_last4(self, instance):
        return f'**** **** **** {instance.last4}'