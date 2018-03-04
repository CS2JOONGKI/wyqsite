from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', login_required(views.PostDetailView.as_view()), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^create/$', views.create, name='create'),
    url(r'^create_post/(?P<user_pk>[0-9]+)/$', views.create_post, name='create_post'),


]
