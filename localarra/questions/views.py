from django.http import Http404
from django.shortcuts import render
from .models import Posts
from django.views import generic

class indexview(generic.ListView):
	template_name = 'questions.html'
	context_object_name = 'all_post'
	paginate_by = 25
	
	def get_queryset(self):
		return Posts.objects.all().filter(PostTypeId = 1).order_by("-CreationDate")

def details(request, posts_id):
	try:
		post_detail = Posts.objects.all().filter(pk = posts_id)
		# for p in post_detail:
		# 	me = p.ParentId
		# pass
		post_details = Posts.objects.all().filter(ParentId = posts_id).exclude(pk = posts_id)
		pass
	except Post.DoesNotExist:
		raise Http404("Ops Whatever you looking is not here")
	return render(request, 'question_detail.html', {'post_detail': post_detail,'post_details' : post_details})

def ohh(request):
	return  render(request,'header.html')