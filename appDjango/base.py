from .models import *
from django.shortcuts import get_object_or_404

def autoriz(login, password):
    users = User.objects.filter(Worker_Login=login, Worker_Password=password)
    return users


def getAnons():
    table = Anons.objects.all()
    return table


def getProduct():
    table1 = Product.objects.all()
    return table1


def getOrder():
    table2 = Order.objects.all()
    return table2


def delete(id):
    get_object_or_404(Anons, id=id)
    product = Anons.objects.get(id=id)
    product.delete()


def deleteproduct(id):
    product1 = Product.objects.get(id=id)
    product1.delete()


def deleteorder(id):
    get_object_or_404(Order, id=id)
    order = Order.objects.get(id=id)
    order.delete()


def get_product_id(id):
    get_object_or_404(Anons, id=id)
    products = Anons.objects.get(id=id)
    return products


def get_user_anons_id(id):
    usersID = Anons.objects.filter(Anons_ID_User=id)
    return usersID


def get_user_order_id(id):
    usersID = Order.objects.filter(Order_Id_User=id)
    return usersID


def loginSearch(login):
    users = User.objects.filter(Worker_Login=login)
    return users


def get_products_id(id):
    get_object_or_404(Product, id=id)
    productss = Product.objects.get(id=id)
    return productss


def get_orders_id(id):
    get_object_or_404(Order, id=id)
    orders = Order.objects.get(id=id)
    return orders


def AddOrder(id):
    OrderSum = Order.objects.filter(id=id).first()
    product = Product.objects.filter(id=OrderSum.Order_Id_Product).first()
    if (product.Product_Sum < OrderSum.Order_Sum):
        return 1
    else:
        ProductMin = product.Product_Sum - OrderSum.Order_Sum
        product.Product_Sum = ProductMin
        product.save()


def update_product(id, nameProduct, SumProduct, DateProduct, PriceProduct, ExpProduct):
    A_anons = Anons.objects.get(id=id)
    A_anons.Anons_NameProducts=nameProduct
    A_anons.Anons_SumProduct=SumProduct
    A_anons.Anons_DateManaProducts=DateProduct
    A_anons.Anons_PriceProduct=PriceProduct
    A_anons.Anons_ExpirationDate=ExpProduct
    A_anons.save()


def update_products(id, nameProduct, SumProduct, PriceProduct ,DateProduct, DateExpirat):
    P_product = Product.objects.get(id=id)
    P_product.Product_Name = nameProduct
    P_product.Product_Sum = SumProduct
    P_product.Product_Price = PriceProduct
    P_product.Product_Production_Date = DateProduct
    P_product.Product_Expiration_Date = DateExpirat
    P_product.save()


def update_orders(id, nameProduct, SumProduct, NameShop, AddressShop, IdProduct):
    O_order = Order.objects.get(id=id)
    O_order.Order_Id_Product = IdProduct
    O_order.Order_Name_Product = nameProduct
    O_order.Order_Sum = SumProduct
    O_order.Order_Name_Store = NameShop
    O_order.Order_Address = AddressShop
    O_order.save()


