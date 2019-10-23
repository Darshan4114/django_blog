from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Blog
from .forms import *
# Create your views here.
def blog_view(request, *args, **kwargs):
    context = {
        "blog_list" : Blog.objects.all()
    }
    return render(request, "blog.html", context)


def blog_detail_view(request, my_id, *args, **kwargs):
    blog = get_object_or_404(Blog, id = my_id)

    context = {
        "blog":blog
    }
    return render(request, "blog_detail.html", context)

def blog_create_view(request,*args, **kwargs):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect ("/success/")
    
    else:
        form = BlogForm()
    return render(request,"blog_create.html",{'form':form})

def success(request,*args, **kwargs): 
    return HttpResponse('successfuly uploaded')