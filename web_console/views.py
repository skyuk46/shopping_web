from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Products, ProductLines, Cart, Feedback
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from datetime import timedelta
import datetime

# Create your views here.
def homepage(request):
    topSellings = Products.objects.order_by('-sold')[:5]
    # Sắp xếp Products theo thứ tự giảm dần của column sold và lấy 5 đối tượng đầu tiên

    carts = []
    try:
        carts = Cart.objects.filter(username = request.user.get_username() )
    except:
        print("Not Login")
    totalPrice = 0
    for cart in carts:
        totalPrice += cart.totalPrice
    quantity = len(carts)
    newToy_raw = Products.objects.filter(status= "New", productLine= "Toy")
    newElectronic_raw = Products.objects.filter(status= "New", productLine= "Electronic")
    newFashion_raw = Products.objects.filter(status= "New", productLine= "Fashion")
    newStationery_raw = Products.objects.filter(status= "New", productLine= "Stationery")

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
                'newStationery' : newStationery,
                'carts' : carts,
                'totalPrice' : totalPrice,
                'quantity' : quantity,
                'topSellings' : topSellings,
                }
    return render(request, 'pages/homepage.html', context)

def blank(request):
    carts = []
    try : 
        carts = Cart.objects.filter(username = request.user.get_username() )
    except:
        print("Not Login")
    totalPrice = 0
    for cart in carts:
        totalPrice += cart.totalPrice
    quantity = len(carts)

    context = { 'carts' : carts,
                'totalPrice' : totalPrice,
                'quantity' : quantity
                }
    return render(request, 'pages/blank.html', context)

def checkout(request):
    carts = []
    try : 
        carts = Cart.objects.filter(username = request.user.get_username() )
    except:
        print("Not Login")
    totalPrice = 0
    for cart in carts:
        totalPrice += cart.totalPrice
    quantity = len(carts)
    totalPriceWithShip = totalPrice + 5

    context = { 'carts' : carts,
                'totalPrice' : totalPrice,
                'quantity' : quantity,
                'totalPriceWithShip' : totalPriceWithShip
                }

    return render(request, 'pages/checkout.html',context)

def product(request):
    carts = []
    try : 
        carts = Cart.objects.filter(username = request.user.get_username() )
    except:
        print("Not Login")
    totalPrice = 0
    for cart in carts:
        totalPrice += cart.totalPrice
    quantity = len(carts)

    name = request.GET.get('product')
    product = Products.objects.get(productName = name)

    relatedProducts = Products.objects.filter(productLine = product.productLine)
    relatedProducts = relatedProducts.order_by('-sold')[:5]
    # Lọc ra những đối tượng có cùng productLine với product sau đó sắp theo theo thứ tự giảm dần của column sold và lấy 5 đối tượng đầu

    # Lọc ra những feedback của product này
    feedbacks = Feedback.objects.filter(product = product.productCode)
    numberOfFeedback = len(feedbacks)
    sumRating = 0
    fiveStarRating = 0
    fourStarRating = 0
    threeStarRating = 0
    twoStarRating = 0
    oneStarRating = 0
    for feedback in feedbacks:
        sumRating += feedback.rating
        if feedback.rating == 5:
            fiveStarRating += 1
        elif feedback.rating == 4:
            fourStarRating += 1
        elif feedback.rating == 3:
            threeStarRating += 1
        elif feedback.rating == 2:
            twoStarRating += 1
        else:
            oneStarRating += 1
    if numberOfFeedback != 0 :
        averageRating = sumRating/numberOfFeedback
        fiveStarRatingPercent = fiveStarRating/numberOfFeedback * 100
        fourStarRatingPercent = fourStarRating/numberOfFeedback * 100
        threeStarRatingPercent = threeStarRating/numberOfFeedback * 100
        twoStarRatingPercent = twoStarRating/numberOfFeedback * 100
        oneStarRatingPercent = oneStarRating/numberOfFeedback * 100
    else:
        averageRating = 5
        fiveStarRatingPercent = 0
        fourStarRatingPercent = 0
        threeStarRatingPercent = 0
        twoStarRatingPercent = 0
        oneStarRatingPercent = 0

    context = { 'carts' : carts,
                'totalPrice' : totalPrice,
                'quantity' : quantity,
                'product' : product,
                'relatedProducts' : relatedProducts,
                'feedbacks' : feedbacks,
                'averageRating' : averageRating,
                'numberOfFeedback' : numberOfFeedback,
                'fiveStarRating' : fiveStarRating,
                'fourStarRating' : fourStarRating,
                'threeStarRating' : threeStarRating,
                'twoStarRating' : twoStarRating,
                'oneStarRating' : oneStarRating,
                'rangeAverageRating' : range(int(averageRating)),
                'fiveStarRatingPercent' : fiveStarRatingPercent,
                'fourStarRatingPercent' : fourStarRatingPercent,
                'threeStarRatingPercent' : threeStarRatingPercent,
                'twoStarRatingPercent' : twoStarRatingPercent,
                'oneStarRatingPercent' : oneStarRatingPercent
                }
    return render(request, 'pages/product.html',context )

def subscribe(request):
    return HttpResponse("Succesfully subscribe!")

def search(request):

    carts = []
    try : 
        carts = Cart.objects.filter(username = request.user.get_username() )
    except:
        print("Not Login")
    totalPrice = 0
    for cart in carts:
        totalPrice += cart.totalPrice
    quantity = len(carts)
    context1 = { 'carts' : carts,
                'totalPrice' : totalPrice,
                'quantity' : quantity,
                'product' : product
                }

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
                     'query': query,
                     'carts' : carts,
                     'totalPrice' : totalPrice,
                     'quantity' : quantity
                     }

            return render(request, 'pages/search.html',context)

        else:
            return render(request, 'pages/search.html',context1)

    else:
        return render(request, 'pages/search.html',context1)    

def upload(request):

	if request.method == 'POST': 
		form = ProductUploadForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return HttpResponse('Successfully uploaded!') 
	else: 
	    form = ProductUploadForm() 
	return render(request, 'pages/upload.html', {'form' : form}) 

def register(request):

    if request.method == "POST":
        form = CustomerRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else: 
	    form = CustomerRegisterForm() 
    return render(request, 'pages/customerRegister.html', {'form' : form})

def addToCart(request):

    if request.method == "GET":
        quantity = int(request.GET.get("quantity"))
        productCode = request.GET.get("productCode")
        salePrice = request.GET.get("sale")
        user = request.user.get_username()
        if user == "" :
            return HttpResponse("Add fail! Please Login")
        product = Products.objects.get(productCode = productCode)
        totalPrice = int(salePrice) * quantity
        id = 1
        if Cart.objects.last():
            id = Cart.objects.last().id + 1
        cart = Cart(id,user,productCode, quantity, totalPrice)
        cart.save()
        return HttpResponse("Added to Cart")

def deleteCartItem(request):

    if request.method == "GET":
        id = int(request.GET.get('cart_product'))
        Cart.objects.get(id = id).delete()
        return HttpResponse('Deleted item from cart')

def placeOrder(request):
    if request.user.get_username() == "":
        return HttpResponse('Please login to place order!')
    else:
        username = request.user.get_username()
        #Save customer information
        name = request.GET.get('first-name') + " " + request.GET.get('last-name')
        email = request.GET.get('email')
        phoneNumber = request.GET.get('tel')
        if Customer.objects.get(username = username):
            customer = Customer.objects.get(username = username)
            customer.numberOfPurchase = customer.numberOfPurchase + 1
        else:
            customer = Customer(username = username,name = name, email = email, phoneNumber = phoneNumber, numberOfPurchase = 1)
        customer.save()


        #Save order information
        carts = Cart.objects.filter(username = username)
        orderedDate = datetime.date.today()
        shippedDate = datetime.date.today() + timedelta(days= 7)
        status = False
        address = request.GET.get('address')
        city = request.GET.get('city')
        country = request.GET.get('country')
        orderNote = request.GET.get('orderNote')
        for cart in carts :
            product = Products.objects.get(productCode = int(cart.product.productCode))
            product.instock -= 1
            product.sold += 1
            product.save()
            cus = Customer.objects.get(username = username)
            Order(product_cart = product,customer = cus,orderedDate = orderedDate,shippedDate = shippedDate,status = status,address = address,city = city,country = country,orderNote = orderNote).save()
            cart.delete()
        return HttpResponse('Your order has been placed. Thank you for Buying ! (If there is nothing in your cart, there will be no order, do not worry')

def feedback(request):
    
    if request.method == "GET":
        name = request.GET.get('customer')
        try:
            customer = Customer.objects.get(name = name)
        except:
            return HttpResponse('Please Buy One Item To Add Feedback')
        productCode = request.GET.get('productCode')
        product = Products.objects.get(productCode = productCode)
        content = request.GET.get('content')
        feedbackDate = datetime.date.today()
        rating = int(request.GET.get('rating'))
        feedback = Feedback(product = product,customer = customer,Content = content,feedbackDate = feedbackDate,rating = rating)
        feedback.save()
        return HttpResponse('Successfully Submit Feedback')
    else:
        return HttpResponse('Please go to product page to add feedback')

