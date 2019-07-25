from django.conf.urls import url, include
from . import views
from . import search
#from .search import BlogSearchListView

urlpatterns = [
    url(r'^$', views.indexview.as_view(), name="index"),
    url(r'^(\d+)$', views.details, name='details'),
    url( r'^search/', search.ajax_search, name = 'blog_search' ),
    url(r'^1/$', views.ohh, name='ohh')
    #url(r'^search/', BlogSearchListView , name='search')
]