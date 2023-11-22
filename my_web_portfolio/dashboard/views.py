from django.http import HttpResponse
from django.template import loader
from .models import Product
from django.shortcuts import render

def dashboard(request):
	template = loader.get_template('dashboard.html')
	return HttpResponse(template.render())

def about(request):
	template = loader.get_template('about.html')
	return HttpResponse(template.render())

def product_details(request):
    try:
        products = Product.objects.all().order_by('description')
        context = {
            'products_list': products,
        }
        return render(request, 'product_details.html', context)
    except Exception as e:
        return render(request, 'product_details.html', {'error_message': str(e)})