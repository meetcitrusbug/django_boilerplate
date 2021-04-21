from rest_framework import serializers
from category.models import SubCategory

class AddSubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'image', 'category']