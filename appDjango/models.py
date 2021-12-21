from django.db import models
from django.utils import timezone


class Anons(models.Model):
    Anons_NameProducts = models.CharField(max_length=25, blank=True, null=True)
    Anons_SumProduct = models.IntegerField(default=0)
    Anons_DateManaProducts = models.DateField(default=timezone.now)
    Anons_ExpirationDate = models.DateField(default=timezone.now)
    Anons_PriceProduct = models.IntegerField(default=0)
    Anons_ID_User = models.IntegerField(default=0)




class User(models.Model):
    Worker_Surname = models.CharField(max_length=50)
    Worker_Name = models.CharField(max_length=50)
    Worker_Patronymic = models.CharField(max_length=50)
    Worker_Number = models.CharField(max_length=11)
    Worker_Position = models.CharField(max_length=20, default='some string')
    Worker_Login = models.CharField(max_length=25, default='some string')
    Worker_Password = models.CharField(max_length=25, default="some string")


class Arrival(models.Model):
    ID_Receipt_Invoice = models.ForeignKey(Anons, on_delete=models.CASCADE)
    ID_Worker = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    Product_Name = models.CharField(max_length=25)
    Product_Price = models.IntegerField(default=0)
    Product_Sum = models.IntegerField(default=0)
    Product_Expiration_Date = models.DateField(default=timezone.now)
    Product_Production_Date = models.DateField(default=timezone.now)
    Product_Arrival_ID = models.ManyToManyField(Arrival)


class Order(models.Model):
    Order_Name_Product = models.CharField(max_length=25, default="")
    Order_Sum = models.IntegerField(default=0)
    Order_Id_Product = models.IntegerField(default=0, blank=True, null=True)
    Order_Name_Store = models.CharField(max_length=25)
    Order_Address = models.CharField(max_length=100)
    Order_Id_User = models.IntegerField(default=0)


class Consumption(models.Model):
    Consumption_Id_Worker = models.ForeignKey(User, on_delete=models.CASCADE)
    Consumption_Id_Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Consumption_Product_ID = models.ManyToManyField(Product)

