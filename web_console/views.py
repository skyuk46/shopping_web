from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Products
from django.http import HttpResponse 
from .forms import *

# Create your views here.
def homepage(request):
    return render(request, 'pages/homepage.html')

def blank(request):
    return render(request, 'pages/blank.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def product(request):
    return render(request, 'pages/product.html')

def store(request):
    return render(request, 'pages/store.html')

def search(request):

    if request.method == 'GET':
        category = request.GET.get('type')
        # get category        
        query= request.GET.get('input')
        # get input
        submitbutton= request.GET.get('submit')
        # get button
        res = Products.objects.get(productCode = 6)
        if query is not None:
            # lookups= Q(title__icontains=query) | Q(content__icontains=query)

            # results= Post.objects.filter(lookups).distinct()
            if category == '0':
               results = Products.objects.filter(productName__icontains = query, description__icontains = query)
            # filter all the product which title and content has word in query in category table
            context={'results': results,
                     'submitbutton': submitbutton,
                     'query': query,
                     'res' : res}

            return render(request, 'pages/search.html',context)

        else:
            return render(request, 'pages/search.html')

    else:
        return render(request, 'pages/search.html')    

def upload(request):

	if request.method == 'POST': 
		form = ProductUploadForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return HttpResponse('Successfully uploaded!') 
	else: 
	    form = ProductUploadForm() 
	return render(request, 'pages/upload.html', {'form' : form}) 


