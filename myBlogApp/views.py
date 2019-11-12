from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_Date__lte=timezone.now()).order_by('published_Date')
    return  render(request,'myBlogApp/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post =get_object_or_404(Post, pk=pk)
    return render(request, 'myBlogApp/post_detail.html', {'post': post})