from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django_boilerplate.helpers import custom_response
from .serializer import MediaCategoryListSerializer, MediaCategoryDetailsSerializer, MediaCategoryCreateSerializer, MediaCategoryUpdateSerializer, MediaImageSerializer, MediaVideoSerializer
from .models import MediaCategory, MediaImage, MediaVideo
from .utils.pagination import CategoryPagination



class MediaCategoryListAPIView(APIView):
    
    permission_classes = (AllowAny,)
    serializer_class = MediaCategoryListSerializer

    def get(self, request):
        categories = MediaCategory.objects.all().order_by('-id')
        serializer = self.serializer_class(categories, many=True, context= {"request": request})
        result={}
        result['categories'] = serializer.data
        message = "All media categories fetched successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)


class MediaCategoryDetailAPIView(ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = MediaCategoryDetailsSerializer
    pagination_class = CategoryPagination
    model = MediaCategory
    queryset = model.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"All categories fetched successfully!",
            "data":serializer.data
        }, status.HTTP_200_OK )
        
    def filter_queryset(self, queryset):
        queryset = queryset.filter(is_active=True)
        return queryset


class MediaCategoryDeleteAPIView(DestroyAPIView):
    queryset = MediaCategory.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Category deleted successfully",
            "data":{}
        }, status.HTTP_200_OK )


class MediaCategoryCreateAPIView(CreateAPIView):
    
    permission_classes = (AllowAny,)
    serializer_class = MediaCategoryCreateSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = self.get_serializer(data=data, context={'request':request})
        serializer = self.get_serializer(context={'request':request})
        is_valid = serializer.is_valid()
        
        if not is_valid:
            return  Response({
                "status":False,
                "code":status.HTTP_200_OK,
                "message":"Please fill missing field or solve error",
                "data":serializer.errors,
                }, status.HTTP_200_OK )
                    
        self.perform_create(serializer)

        return  Response({
                    "status":True,
                    "code":status.HTTP_200_OK,
                    "message":"New category created successfully",
                    "data":serializer.data,
                    }, status.HTTP_200_OK )


class MediaCategoryUpdateAPIView(UpdateAPIView):
    
    permission_classes = (AllowAny,)
    queryset = MediaCategory.objects.all()
    serializer_class = MediaCategoryUpdateSerializer
    lookup_field = 'id'


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        is_valid = serializer.is_valid()
        
        if not is_valid: 
            return  Response({"status":False,
                            "code":status.HTTP_200_OK,
                            "message":"Please fill missing field or solve error",
                            "data":serializer.errors,
                            }, status.HTTP_200_OK )
            
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return  Response({ "status":True,
                        "code":status.HTTP_200_OK,
                        "message":"Category updated successfully",
                        "data":serializer.data,
                        }, status.HTTP_200_OK )



# =================== Images API =================== # 
class MediaImageAddAPIView(CreateAPIView):
    
    permission_classes = (AllowAny,)
    queryset = MediaImage.objects.all()
    serializer_class = MediaImageSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = self.get_serializer(data=data, context={'request':request})
        is_valid = serializer.is_valid()
        
        if not is_valid:
            return  Response({
                "status":False,
                "code":status.HTTP_200_OK,
                "message":"Please fill missing field or solve error",
                "data":serializer.errors,
                }, status.HTTP_200_OK )
                    
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return  Response({
                    "status":True,
                    "code":status.HTTP_200_OK,
                    "message":"Media image added successfully!",
                    "data":serializer.data,
                    }, status.HTTP_200_OK )



class MediaImageDeleteAPIView(DestroyAPIView):
    
    permission_classes = (AllowAny,)
    queryset = MediaImage.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Media image deleted successfully!",
            "data":{}
        }, status.HTTP_200_OK )



# =================== Videos API =================== # 
class MediaVideoAddAPIView(CreateAPIView):
    
    permission_classes = (AllowAny,)
    queryset = MediaVideo.objects.all()
    serializer_class = MediaVideoSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = self.get_serializer(data=data, context={'request':request})
        is_valid = serializer.is_valid()
        
        if not is_valid:
            return  Response({
                "status":False,
                "code":status.HTTP_200_OK,
                "message":"Please fill missing field or solve error",
                "data":serializer.errors,
                }, status.HTTP_200_OK )
                    
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return  Response({
                    "status":True,
                    "code":status.HTTP_200_OK,
                    "message":"Media video added successfully!",
                    "data":serializer.data,
                    }, status.HTTP_200_OK )



class MediaVideoDeleteAPIView(DestroyAPIView):
    
    permission_classes = (AllowAny,)
    queryset = MediaVideo.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Media video deleted successfully!",
            "data":{}
        }, status.HTTP_200_OK )