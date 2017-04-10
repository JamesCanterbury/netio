from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):	
	posts=Post.objects.filter()
	return render(request, 'blog/post_list.html', {'posts' : posts})
def post_detail(request, pk):
	Post.objects.get(pk=pk)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

	#Old Way   -posts = Post.objects.filter()
	## old way -return render(request, 'blog/post_list.html', {'posts' : posts})
	#posts = Post.objects.filter(published_date=timezone.now()).order_by('published_date')
