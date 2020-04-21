from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.homepage),
   path('blank/', views.blank),
   path('checkout/', views.checkout),
   path('product/', views.product),
   path('store/', include('product_list.urls')),
   path('search/', views.search),
   path('upload/', views.upload),
   path('subscribe/', views.subscribe)
]