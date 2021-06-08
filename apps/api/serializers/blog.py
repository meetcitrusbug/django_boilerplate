from rest_framework import serializers
from Blog.models import Blog

# Serializers for creating Blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'