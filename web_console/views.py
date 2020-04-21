from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Products, ProductLines
from django.http import HttpResponse 
from .forms import *

# Create your views here.
def homepage(request):
    newToy_raw = Products.objects.filter(status = "New", productLine = "Toy")
    newElectronic_raw = Products.objects.filter(status = "New", productLine = "Electronic")
    newFashion_raw = Products.objects.filter(status = "New", productLine = "Fashion")
    newStationery_raw = Products.objects.filter(status = "New", productLine = "Stationery")

    if len(newToy_raw) <= 5:
        newToy = newToy_raw
    else:
        newToy = newToy_raw[0:5]

    if len(newElectronic_raw) <= 5:
        newElectronic = newElectronic_raw
    else:
        newElectronic = newElectronic_raw[0:5]

    if len(newFashion_raw) <= 5:
        newFashion = newFashion_raw
    else:
        newFashion = newFashion_raw[0:5]

    if len(newStationery_raw) <= 5:
        newStationery = newStationery_raw
    else:
        newStationery = newStationery_raw[0:5]

    context = { 'newToy' : newToy,
                'newElectronic' : newElectronic,
                'newFashion' : newFashion,
                'newStationery' : newStationery
                }
    return render(request, 'pages/homepage.html',context)

def blank(request):
    return render(request, 'pages/blank.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def product(request):
    name = request.GET.get('product')
    product = Products.objects.get(productName = name)
    return render(request, 'pages/product.html',{'product': product })

def subscribe(request):
    return HttpResponse("Succesfully subscribe!")

def search(request):

    if request.method == 'GET':
        category = request.GET.get('type')
        # get category        
        query= request.GET.get('input')
        # get input
        submitbutton= request.GET.get('submit')
        # get button
        if query is not None:
            # lookups= Q(title__icontains=query) | Q(content__icontains=query)

            # results= Post.objects.filter(lookups).distinct()
            if category == '1':
               results = Products.objects.filter(productName__icontains = query,productLine = "Toy")
            elif category == '2':
               results = Products.objects.filter(productName__icontains = query,productLine = "Electronic")
            elif category == '3':
               results = Products.objects.filter(productName__icontains = query,productLine = "Household")
            elif category == '4':
               results = Products.objects.filter(productName__icontains = query,productLine = "Fashion")
            elif category == '5':
               results = Products.objects.filter(productName__icontains = query,productLine = "Sporting")
            elif category == '6':
               results = Products.objects.filter(productName__icontains = query,productLine = "Stationery")
            else :
               results = Products.objects.filter(productName__icontains = query)

            # filter all the product which title and content has word in query in category table
            context={'results': results,
                     'submitbutton': submitbutton,
                     'query': query}

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


