from django.http import HttpResponse
from django.template import loader

def dashboard(request):
	template = loader.get_template('dash.html')
	return HttpResponse(template.render())