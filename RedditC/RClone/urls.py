from django.conf.urls import url, include
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls')),
    url(r'^post/', include('posts.urls')),
    url(r'^$', views.home, name="home")

]
