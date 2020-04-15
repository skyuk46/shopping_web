from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage),
   path('blank/', views.blank),
   path('checkout/', views.checkout),
   path('product/', views.product),
   path('store/', views.store),
   path('search/', views.search),
   path('upload/', views.upload),
]