from rest_framework import serializers
from category.models import Category


class AddCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']