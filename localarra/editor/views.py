from django.shortcuts import render

def index(request):
	return render(request, 'editor/editor.html')

def ajax_result(request):
	if request.is_ajax():
		editor_result = request.GET.get( 'content' )
		print (editor_result)
	return render(request, 'editor/pass.html', { 'editor_result': editor_result, })