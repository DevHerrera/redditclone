from django.conf.urls import url
import posts.views

app_name = 'posts'
urlpatterns = [
	url(r'^create/', posts.views.create, name = 'create'),
	url(r'(?P<pk>[0-9]+)/upvote', posts.views.upvote, name = 'upvote'),
	url(r'(?P<pk>[0-9]+)/downvote', posts.views.downvote, name = 'downvote'),
	url(r'^user/(?P<fk>[0-9]+)', posts.views.userposts, name='userposts'),

]
