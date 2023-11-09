from django.http import HttpResponse
from django.template import loader

def comments(request):
	template = loader.get_template('comments.html')
	return HttpResponse(template.render())
