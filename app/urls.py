from django.urls import path
from .views import landingview, productlistview, supplierslistview, addsupplier, addproduct
from .views import deleteproduct, confirmdeleteproduct, edit_product_get, edit_product_post
from .views import searchsuppliers, products_filtered, confirmdeletesupplier, deletesupplier
from .views import loginview, login_action, logout_action
urlpatterns = [
    path('', landingview),

    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),
    
    path('suppliers/', supplierslistview),
    path('add-supplier/', addsupplier),
    path('search-suppliers/', searchsuppliers),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
]
