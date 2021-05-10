from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BlogForm
from .models import Blog
from django.db.models import Q

# Create your views here.
class BlogListingView(View):
    def get(self,request):
        blog = Blog.objects.all()
        return render(request,'index.html',{'blog':blog})

class CreateBlogView(View):
    def get(self,request):
        form = BlogForm()
        return render(request,'blog/create-blog.html',{"form":form})

    def post(self,request):
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            HttpResponse('Your Data Is Not Valid')
        return render(request,'blog/create-blog.html',{"form":form})

class BlogDetailView(View):
    def get(self,request,blog_id):
        blog = Blog.objects.get(pk=blog_id)
        return render(request,'blog/blog-detail.html',{"blog":blog})

class BlogUpdateView(View):
    def get(self,request,blog_id):
        blog = Blog.objects.get(pk=blog_id)
        form = BlogForm(instance=blog)
        return render(request,'blog/create-blog.html',{"form":form})

    def post(self,request,blog_id):
        blog = Blog.objects.get(pk=blog_id)
        form = BlogForm(data=request.POST, files=request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            HttpResponse('Your Data Is Not Valid')
        return render(request,'blog/create-blog.html',{"form":form})

class BlogSearchView(View):
    def get(self,request):
        blog_content = request.GET.get('blog_content')
        category = request.GET.get('category')
        month = request.GET.get('month')
        if blog_content:
            blog = Blog.objects.filter(Q(blog_title__icontains=blog_content) | Q(keyword__icontains=blog_content)
                                       | Q(publish__year__icontains=blog_content))
        if category:
            blog = Blog.objects.filter(Q(category__category=category))
        if month:
            blog = Blog.objects.filter(Q(publish__month=month))
        
        return render(request,'blog/blog-search.html',{'blog':blog})