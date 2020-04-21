from django.urls import path, include
from . import views

urlpatterns = [
   path('toy/', views.store,{ 'productLine' : 'Toy' }),
   path('electronic/', views.store,{ 'productLine' : 'Electronic' }),
   path('household/', views.store,{ 'productLine' : 'Household' }),
   path('fashion/', views.store,{ 'productLine' : 'Fashion' }),
   path('sporting/', views.store,{ 'productLine' : 'Sporting' }),
   path('stationery/', views.store,{ 'productLine' : 'Stationery' }),
]