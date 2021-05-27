from rest_framework.generics import ListAPIView
from order.models import UserCard
from order.serializers import CardListSerializer
from rest_framework.permissions import IsAuthenticated

class CardListAPIView(ListAPIView):
    
    serializer_class = CardListSerializer
    permission_classes = [IsAuthenticated]
        
    def get_queryset(self):
        return UserCard.objects.filter(user=self.request.user).order_by('-id')