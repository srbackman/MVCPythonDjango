from django.urls import path
from .views import landingview, productlistview, supplierslistview, addsupplier, addproduct

urlpatterns = [
    path('', landingview),
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('suppliers/', supplierslistview),
    path('add-supplier/', addsupplier),
]
