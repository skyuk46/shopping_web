from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage),
    path('blank/', views.blank),
    path('checkout/', views.checkout),
    path('product/', views.product),
    path('store/', include('product_list.urls')),
    path('search/', views.search),
    path('upload/', views.upload),
    path('subscribe/', views.subscribe),
    path('customerRegister', views.register),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('product/addToCart/', views.addToCart),
    path('deleteCartItem/', views.deleteCartItem),
    path('placeOrder/', views.placeOrder),
    path('feedback/', views.feedback),
]
