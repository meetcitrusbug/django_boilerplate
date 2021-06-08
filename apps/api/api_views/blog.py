from Blog.models import Blog, BlogKeyword
from ..serializers.blog import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class BlogListView(ListAPIView):
    serializer_class = BlogSerializer
    model = Blog
    queryset = model.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Blogs fetch successfully",
            "data":serializer.data
        }, status.HTTP_200_OK )
        
    def filter_queryset(self, queryset):
        
        search = self.request.query_params.get('search')
        year = self.request.query_params.get('year')
        category = self.request.query_params.get('category')

        if search:
            keyword = BlogKeyword.objects.filter(keyword__icontains=search).values_list('blog', flat=True)
            queryset = queryset.filter(Q(id__in=keyword) | Q(blog_title__icontains=search))
        if year:
            queryset = queryset.filter(created_at__date__year=year)
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset

class BlogDetailView(RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        message = 'Blog fetch successfully'
        status_ =  True
        if not instance:
            message ='Blog doesn"t found'
            status_ = False
            
        serializer = self.get_serializer(instance, context={'request':request})
        return  Response({
                    "status":status_,
                    "code":status.HTTP_200_OK,
                    "message":message,
                    "data":serializer.data if status_ else {},
                    }, status.HTTP_200_OK )
        
    def get_object(self):
        id = self.kwargs.get('id')
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return None


class BlogCreateView(CreateAPIView):
    serializer_class = BlogSerializer
    
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

        return  Response({
                    "status":True,
                    "code":status.HTTP_200_OK,
                    "message":"Blog created successfully",
                    "data":serializer.data,
                    }, status.HTTP_200_OK )


class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
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
                        "message":"Blog updated successfully",
                        "data":serializer.data,
                        }, status.HTTP_200_OK )


class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Blog deleted successfully",
            "data":{}
        }, status.HTTP_200_OK )