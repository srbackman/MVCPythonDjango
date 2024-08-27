from django.db import models

class Supplier(models.Model):
    companyName = models.CharField(max_length = 50, default = "firma")
    contactName = models.CharField(max_length = 50, default = "firma")
    address = models.CharField(max_length = 100, default = "osoite")
    phone = models.CharField(max_length = 20, default = "puhelin")
    email = models.CharField(max_length = 50, default = "sähköposti")
    country = models.CharField(max_length = 50, default = "maa")

    def __str__(self):
        return (f"{self.companyName} from {self.country}")

class Product(models.Model):
    productName = models.CharField(max_length = 20, default = "laku")
    packageSize = models.CharField(max_length = 20, default = 3)
    unitPrice = models.DecimalField(max_digits = 8, decimal_places = 2, default = 1.00)
    unitsInStock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)

    def __str__(self):
        return (f"{self.productName} produced by {self.supplier.companyName}")