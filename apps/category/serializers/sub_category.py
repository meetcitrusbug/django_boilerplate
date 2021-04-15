from rest_framework import serializers
from category.models import SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'image']