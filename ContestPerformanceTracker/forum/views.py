from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url='login')
def view_post(request):
    posts=Post.objects.all()
    print(posts)


    return render(request,'post.html',{'posts':posts})


@login_required(login_url='login')
def post_detail(request,slug):
    post=Post.objects.get(slug=slug)

    return render(request,'postdetail.html',{'post':post})

