from rest_framework import serializers
from .models import MediaCategory, MediaImage, MediaVideo


# ===================== List ===================== #
class MediaCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCategory
        fields = ('id', 'category', 'created_at')

class MediaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ['id', 'image', 'category', 'created_at']


class MediaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaVideo
        fields = ['id', 'video', 'category', 'created_at']


# ===================== Detail ===================== #
class MediaCategoryDetailsSerializer(serializers.ModelSerializer):    
    image = serializers.SerializerMethodField('get_image')
    video = serializers.SerializerMethodField('get_video')

    class Meta:
        model = MediaCategory
        fields = ['id', 'category', 'image', 'video']
        
    def get_image(self, obj):
        image_obj = MediaImage.objects.select_related('category').filter(category=obj.id)
        images = []
        if image_obj:
            for img in image_obj:
                images.append(img.image.url)
            return images
        return ''

    def get_video(self, obj):
        video_obj = MediaVideo.objects.select_related('category').filter(category=obj.id)
        videos = []
        if video_obj:
            for vid in video_obj:
                videos.append(vid.video.url)
            return videos
        return ''


# ===================== Create ===================== #
class MediaCategoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MediaCategory
        fields = ['id', 'category']

        
    def save(self, *args, **kwargs):
        instance = super(MediaCategoryCreateSerializer, self).save()
        
        request = self.context.get('request')
        images = request.data.getlist('image')
        videos = request.data.getlist('video')
        
        media_image_data = []
        media_video_data = []
        
        for image in images:
            media_image_data.append({
                            'image':image,
                            'category':instance.pk})

        for video in videos:
            media_video_data.append({
                            'video':video,
                            'category':instance.pk})
        
            
        # Save multiple images
        self.image_serializer = MediaImageSerializer(
                    data=media_image_data, many=True)
        self.image_serializer.is_valid()
        self.image_instances = self.image_serializer.save()
        
        # Save multiple videos
        self.video_serializer = MediaVideoSerializer(
                    data=media_video_data, many=True)
        self.video_serializer.is_valid()
        self.video_instances = self.video_serializer.save()
                
        return instance
    
    def to_representation(self, instance):
        result = super(MediaCategoryCreateSerializer, self).to_representation(instance)
        result['images']= self.image_serializer.to_representation(self.image_instances)
        result['videos']= self.video_serializer.to_representation(self.video_instances)
        return result



# ===================== Update ===================== #
class MediaCategoryUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MediaCategory
        fields = ['id', 'category']

    def save(self, *args, **kwargs):
        instance = super(MediaCategoryUpdateSerializer, self).save()
        return instance

# ---------------------- Image Update ---------------------- #
class MediaImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ['id', 'image', 'category']

    def save(self, *args, **kwargs):
        instance = super(MediaImageUpdateSerializer, self).save()
        return instance

# ---------------------- Video Update ---------------------- #
class MediaVideoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaVideo
        fields = ['id', 'video', 'category']

    def save(self, *args, **kwargs):
        instance = super(MediaVideoUpdateSerializer, self).save()
        return instance