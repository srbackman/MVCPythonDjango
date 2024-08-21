from django.shortcuts import render, redirect
from app.models import Supplier, Product

def landingview(request):
    return(render(request, 'landingpage.html'))


#Products
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return(render(request, 'productlist.html', context))

def addproduct(request):
    a = request.POST['productName']
    b = request.POST['packageSize']
    c = request.POST['unitPrice']
    d = request.POST['unitsInStock']
    e = request.POST['supplier']

    Product(productName = a, packageSize = b, unitPrice = c, unitsInStock = d, supplier = Supplier.objects.get(id = e)).save()
    return (redirect(request.META['HTTP_REFERER']))

#Suppliers
def supplierslistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return(render(request, 'supplierslist.html', context))

def addsupplier(request):
    a = request.POST['companyName']
    b = request.POST['contactName']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']

    Supplier(companyName = a, contactName = b, address = c, phone = d, email = e, country = f).save()
    return (redirect(request.META['HTTP_REFERER']))
