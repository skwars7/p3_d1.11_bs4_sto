from django.conf.urls import url, include
from . import stack

urlpatterns = [
    url(r'^$', stack.index, name='index'),
]