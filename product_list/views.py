from django.shortcuts import render
from web_console.models import Products, Cart

# Create your views here.
def store(request,productLine):
    carts = []
    try : 
        carts = Cart.objects.filter(username = request.user.get_username() )
    except:
        print("Not Login")
    totalPrice = 0
    for cart in carts:
        totalPrice += cart.totalPrice
    quantity = len(carts)

    products = Products.objects.filter(productLine = productLine)
    topSellings = products.order_by('-sold')[:5]
    length = len(products)
    count = 0
    tab1 = 0
    tab2 = 0
    tab3 = 0
    tab4 = 0
    product1 = []
    product2 = []
    product3 = []
    product4 = []
    if length <= 9:
        tab1 = length
        product1 = products[0 : tab1]
    else :
        tab1 = 9
        product1 = products[0 : tab1]
        if (length - tab1) <= 9:
            tab2 = length
            product2 = products[tab1 : tab2]
        else:
            tab2 = 18
            product2 = products[tab1 : tab2]
            if (length - tab2) <= 9:
                tab3 = length
                product3 = products[tab2 : tab3]
            else:
                tab3 = 27
                product3 = products[tab2 : tab3]
                tab4 = length
                products4 = products[tab3 : tab4]
    return render(request, 'pages/store.html',{'topSellings' : topSellings,'carts' : carts,'totalPrice' : totalPrice,'quantity' : quantity,'products': products, 'productLine': productLine,'length': length, 'count': count, 'tab1' : tab1,'tab2' : tab2,'tab3' : tab3,'tab4' : tab4,'product1': product1,'product2': product2,'product3': product3,'product4': product4})

