from django.shortcuts import render, redirect
from app.models import Supplier, Product
from django.contrib.auth import authenticate, login, logout

#Landing view
def landingview(request):
    return(render(request, 'landingpage.html'))

#Login & logout
def loginview(request):
    return(render(request, 'loginpage.html'))

def login_action(request):
    user = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = user, password = password)
    if (user):
        login(request, user)
        context = {'name' : user}
        return(render(request, 'landingpage.html', context))
    else:
        return(render(request, 'loginerror.html'))
    
def logout_action(request):
    logout(request)
    return(render(request, 'loginpage.html'))

#----------------------------------------Products----------------------------------------
def productlistview(request):
    if (not request.user.is_authenticated):
        return (render(request, 'loginpage.html'))
    else:
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

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return (render(request, "confirmdeleteproduct.html", context))

def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return (redirect(productlistview))

def edit_product_get(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return (render(request, "edit_product.html", context))

def edit_product_post(request, id):
    item = Product.objects.get(id = id)
    item.unitPrice = request.POST['unitPrice']
    item.unitsInStock = request.POST['unitsInStock']
    item.save()
    return (redirect(productlistview))

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return (render(request, "productlist.html",context))

#----------------------------------------Suppliers----------------------------------------
def supplierslistview(request):
    if (not request.user.is_authenticated):
        return (render(request, 'loginpage.html'))
    else:
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

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyName__icontains = search)
    context = {'suppliers': filtered}
    return (render(request, "supplierslist.html", context))

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return (render(request, "confirmdeletesupplier.html", context))

def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return (redirect(supplierslistview))