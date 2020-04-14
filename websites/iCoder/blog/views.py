from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    # print(allposts)
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)
    # return HttpResponse("This is BlogHome")


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    # print(post)
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f"This is Blog: {slug}")
