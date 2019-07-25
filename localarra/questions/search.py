from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Posts
import time

def ajax_search( request ):

    if request.is_ajax():
        q = request.GET.get( 'q' )
        print(q)
        if q is not None:            
            # results = User.objects.filter( 
            #     Q( first_name__contains = q ) |
            #     Q( last_name__contains = q ) |
            #     Q( username__contains = q ) ).order_by( 'username' )
            results = Posts.objects.filter( 
                Q( Tags__contains = q ) |
                Q( Title__contains = q ) |
                Q( Body__contains = q ) ).filter( PostTypeId = 1 ).order_by( 'Title' )
    return render(request, 'result.html', { 'results': results, })