from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost

# Create your views here.
def index(request):
    myposts = blogPost.objects.all()
    return render(request, 'blog/index.html',{'myposts':myposts})

def blogpost(request, id):
    post=blogPost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogPost.html', {'post':post})
