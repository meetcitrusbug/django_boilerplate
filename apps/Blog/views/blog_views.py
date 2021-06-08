from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from ..forms import BlogForm
from ..models import Blog, Category, BlogKeyword
from django.db.models import Q
from django.core.files.base import ContentFile
import base64
from datetime import date, timedelta, datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
class BlogListingView(View):
    def get(self,request):
        blog = Blog.objects.all()
        category = Category.objects.all()
        return render(request,'index.html',{'blog':blog,'category':category,'user':request.user})

class CreateBlogView(View):
    def get(self,request):
        if (not request.user.is_authenticated) or (request.user.is_staff):
            return redirect('login')
        category = Category.objects.all()
        form = BlogForm()
        return render(request,'blog/create-blog.html',{"form":form,'category':category})

    def post(self,request):
        category = Category.objects.get(pk=request.POST.get('category'))
        blog_title = request.POST.get('blog_title')
        blog = request.POST.get('blog')
        blog_id = request.POST.get('exist_blog')
        keywords = request.POST.getlist('keyword[]')
        author = request.POST.get('author')
        document_file = request.POST.get('document_image')
        if 'base64' in document_file:
            formated_string, imgstr = document_file.split(';base64,')
            ext = formated_string.split('/')[-1]
            image_file = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        else:
            image_file =document_file.split('/')[-1]
        
        
        if blog_id:
            exist_blog = Blog.objects.get(pk=blog_id)
            exist_blog.blog_title = blog_title
            exist_blog.blog = blog
            exist_blog.category = category
            exist_blog.author = author
            exist_blog.image = image_file
            exist_blog.save()
            response = {
                'message':'Updated successfully',
                'status':True
            }
            return JsonResponse(response)
        blog = Blog(
            blog_title=blog_title,
            blog=blog,
            category=category,
            author=author,
            image=image_file,
            user=request.user
        )
        blog.save()
        for keyword in keywords:
            if keyword:
                BlogKeyword.objects.create(blog=blog,keyword=keyword)
        response = {
            'message':'Created successfully',
            'status':True
        }
        return JsonResponse(response)

class BlogDetailView(View):
    def get(self,request,blog_id):
        if (not request.user.is_authenticated) or (request.user.is_staff):
            return redirect('login')
        blog = Blog.objects.get(pk=blog_id)
        return render(request,'blog/blog-detail.html',{"blog":blog})

class BlogUpdateView(View):
    def get(self,request,blog_id):
        if (not request.user.is_authenticated) or (request.user.is_staff):
            return redirect('login')
        blog = Blog.objects.get(pk=blog_id)
        category = Category.objects.all().exclude(category=blog.category)
        keywords = BlogKeyword.objects.filter(blog=blog)
        return render(request,'blog/update-blog.html',{'blog':blog,'keywords':keywords,'category':category,'user':request.user})

class BlogSearchView(View):
    def get(self,request):
        blog_content = request.GET.get('blog_content')
        category_id = request.GET.get('category_id')
        year = request.GET.get('year')
        
        blog = Blog.objects.all()
        keyword = BlogKeyword.objects.none()
        if blog_content:
            blog = blog.filter(blog_title__icontains=blog_content)
            keyword = BlogKeyword.objects.filter(keyword__icontains=blog_content)
        if category_id:
            blog = blog.filter(category_id=category_id)
        if year:
            blog = blog.filter(created_at__year=year)
        return render(request,'blog/blog-search.html',{'blog':blog,'keyword':keyword})

class LoginPageView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="blog/userlogin.html", context={"login_form":form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                return redirect('login')
        else:
            return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('/')