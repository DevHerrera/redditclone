from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone

@login_required(login_url = '/account/login/')
def create(request):
	if request.POST:
		if request.POST['tittle'] and request.POST['url']:
			url = request.POST['url']
			if url.startswith('http://') or url.startswith('https://'):
				pass
			else:
				url = 'http://' + url
			post = Post(tittle=request.POST['tittle'],
				url=url,
				pub_date=timezone.datetime.now(),
				author=request.user)
			post.save()
			return redirect('home')

		else:
			return render(request, 'posts/create.html', {'message': 'You must provide a tittle and url'})
	return render(request, 'posts/create.html')

def home(request):
	recent_posts = Post.objects.order_by('-votes_total')
	return render(request, 'posts/home.html', {'recent_posts':recent_posts})

def upvote(request, pk):
	if request.POST:
		post = Post.objects.get(id = pk)
		post.votes_total += 1
		post.save()
	return redirect('home')

def downvote(request, pk):
	if request.POST:
		post = Post.objects.get(id = pk)
		post.votes_total -= 1
		post.save()
	return redirect('home')

def userposts(request, fk):
    posts = Post.objects.filter(author__id=fk).order_by('-votes_total')
    author = User.objects.get(pk=fk)
    return render(request, 'posts/userposts.html', {'posts':posts, 'author':author})