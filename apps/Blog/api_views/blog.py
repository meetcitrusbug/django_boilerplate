from ..models import Blog
from ..serializers.blog import BlogSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def BlogListView(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def BlogDetailView(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    serializer = BlogSerializer(blog)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def BlogCreateView(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    # else:
    #     print("issue with data")
    # print(serializer.errors)
    # print(serializer.data)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def BlogUpdateView(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    serializer = BlogSerializer(instance=blog,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def BlogDeleteView(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()

    return JsonResponse('Your Data Is Deleted!',safe=False)