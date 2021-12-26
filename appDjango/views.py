from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .base import *
from django.shortcuts import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.contrib import messages


def error_404(request, exception):
    context = {
        'Privel': request.session['priv_user']
    }
    return render(request, '404.html', context)


class Login(View):
    def get(self, request):
        context = {

        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        entered_login = request.POST.get("login")
        entered_passw = request.POST.get("password")
        users = autoriz(entered_login, entered_passw)
        if not users:
            context = {
                "message": "Введен неверный логин или пароль"
            }
            return render(request, 'login.html', context=context)
        elif users[0].Worker_Position == "Поставщик":
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].Worker_Position
            return HttpResponseRedirect('/sitePostavshik/stieaccpostavshik.html')
        elif users[0].Worker_Position == "Менеджер магазина":
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].Worker_Position
            return HttpResponseRedirect('/siteshop/stieaccshop.html')
        else:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].Worker_Position
            return HttpResponseRedirect('/stieacc.html')


class Registration(View):
    def get(self, request):
        context = {

        }
        return render(request, 'registration.html', context=context)

    def post(self, request):
        user_surname = request.POST['SurName']
        user_name = request.POST['Name']
        user_aftername = request.POST['AfterName']
        user_login = request.POST['Login']
        user_phone = request.POST['Phone']
        user_pass = request.POST['Pass']
        position_user = request.POST.get("Pos")
        LoginUser = request.POST.get("Login")
        loginSearchs = loginSearch(LoginUser)
        if loginSearchs:
            context = {
                "message": "Логин уже занят"
            }
            return render(request, 'registration.html', context=context)
        else:
            if position_user == "Поставщик":
                user_role = "Поставщик"
            else:
                user_role = "Менеджер магазина"
            create_anons = User( Worker_Surname=user_surname, Worker_Name=user_name,
                                 Worker_Patronymic= user_aftername,
                                 Worker_Login=user_login,
                                 Worker_Number=user_phone,
                                 Worker_Password = user_pass,
                                 Worker_Position = user_role)
            create_anons.save()
            return HttpResponseRedirect('login.html')


class RegistrationPostav(View):
    def get(self, request):
        context = {

        }
        return render(request, 'registrationPostav.html', context=context)

    def post(self, request):
        user_surname = request.POST['SurName']
        user_name = request.POST['Name']
        user_aftername = request.POST['AfterName']
        user_login = request.POST['Login']
        user_phone = request.POST['Phone']
        user_pass = request.POST['Pass']
        LoginUser = request.POST.get("Login")
        loginSearchs = loginSearch(LoginUser)
        if loginSearchs:
            context = {
                "message": "Логин уже занят"
            }
            return render(request, 'registrationPostav.html', context=context)
        else:
            user_role = "Менеджер склада"
            create_anons = User( Worker_Surname=user_surname, Worker_Name=user_name,
                                 Worker_Patronymic= user_aftername,
                                 Worker_Login=user_login,
                                 Worker_Number=user_phone,
                                 Worker_Password = user_pass,
                                 Worker_Position = user_role)
            create_anons.save()
            return HttpResponseRedirect('login.html')


class SiteAnons(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер склада"):
                    tablesee = getAnons()
                    context = {
                        'tablesee': tablesee
                    }
                    return render(request, 'siteannons.html', context=context)
                else:
                    return HttpResponseRedirect("ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("login.html")

    def post(self, request):
        id = request.POST.get("id")
        if id:
            if request.POST.get("deleteproduct"):
                delete(id)
                return HttpResponseRedirect('siteannons.html')
            elif request.POST.get("addproduct"):
                tablesee1 = get_product_id(id)
                create_product = Product(Product_Name = tablesee1.Anons_NameProducts,
                                          Product_Price = tablesee1.Anons_PriceProduct,
                                          Product_Sum = tablesee1.Anons_SumProduct,
                                          Product_Production_Date = tablesee1.Anons_DateManaProducts,
                                          Product_Expiration_Date = tablesee1.Anons_ExpirationDate
                                          )
                create_product.save()
                delete(id)
                return HttpResponseRedirect('siteannons.html')
            else:
                tablesee = getAnons()
                context = {
                    'tablesee': tablesee
                }
                return render(request, 'siteannons.html', context=context)
        else:
            tablesee = getAnons()
            context = {
                  'tablesee': tablesee
             }
            return render(request, 'siteannons.html', context=context)


class SiteOrder(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер склада"):
                    shopsee = getOrder()
                    context = {
                        'shopsee': shopsee
                    }
                    return render(request, 'siteorder.html', context=context)
                else:
                    return HttpResponseRedirect("ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("login.html")

    def post(self, request):
        id = request.POST.get("id")
        if id:
            if request.POST.get("DeleteProduct"):
                deleteorder(id)
                return HttpResponseRedirect('siteorder.html')
            elif request.POST.get("AddProduct"):
                get_object_or_404(Order, id=id)
                OrderSum = Order.objects.filter(id=id).first()
                if (Product.objects.filter(id=OrderSum.Order_Id_Product).exists()):
                    bullOrder = AddOrder(id)
                    if (bullOrder == 1):
                        deleteorder(id)
                        return HttpResponseRedirect("ErrorSiteProducts.html")
                    else:
                        deleteorder(id)
                        messages.success(request, "Заказ успешно выполнен")
                        return HttpResponseRedirect('siteorder.html')

                else:
                    deleteorder(id)
                    return HttpResponseRedirect("ErrorSiteProducts.html")

        else:
            shopsee = getOrder()
            context = {
                'shopsee': shopsee
            }
            return render(request, 'siteorder.html', context=context)


class ProductSite(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер склада"):
                    productsee = getProduct()
                    context = {
                            'productsee': productsee
                        }
                    return render(request, 'productssite.html', context=context)
                else:
                    return HttpResponseRedirect("ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("login.html")

    def post(self,request):
        id = request.POST.get("id")
        if id:
            idProducts = get_products_id(id)
            if request.POST.get("deleteproducts"):
                deleteproduct(id)
                return HttpResponseRedirect( 'productssite.html')
            elif request.POST.get("updateproduct"):
                context = {
                    'idProducts': idProducts

                }
                return render(request, 'ProductUpdate.html', context=context)
            elif request.POST.get("updateproduct1"):
                id = request.POST.get("id")
                nameProduct = request.POST.get("Name")
                SumProduct = request.POST.get("Sum")
                PriceProduct = request.POST.get("Price")
                DateProduct = request.POST.get("DateMan")
                DateExpirat = request.POST.get("DateExpirat")
                if (DateExpirat < DateProduct):
                    context = {
                        'idProducts': idProducts,
                        "message": "Срок годности не должен быть меньше чем дата изготовления"
                    }
                    return render(request, 'ProductUpdate.html', context=context)
                update_products(id, nameProduct, SumProduct, PriceProduct ,DateProduct, DateExpirat)
                productsee = getProduct()
                context = {
                    'productsee': productsee
                }
                return render(request, 'productssite.html', context=context)
        else:
            productsee = getProduct()
            context = {
                'productsee': productsee
            }
            return render(request, 'productssite.html', context=context)


class ProductUpdate(View):
    def get(self, request):
        context = {

        }
        return render(request, 'MainSite/services.html', context=context)

class SiteAcc(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер склада"):
                    context = {

                    }
                    return render(request, 'stieacc.html', context=context)
                else:
                    return HttpResponseRedirect("ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("login.html")



class PostavshikProduct(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Поставщик"):
                    context = {

                    }
                    return render(request, 'sitePostavshik/prouductposta.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")

    def post(self, request):
        nameproduct = request.POST['Name']
        sumproduct = request.POST['Sum']
        dateproduct = request.POST['DateMan']
        dateExpProduct = request.POST['DateExpMan']
        priceproduct = request.POST['Price']
        UserID = request.session['id_user']
        if (dateExpProduct <= dateproduct):
            context = {
                "message": "Срок годности не должен быть меньше чем дата изготовления"
            }
            return render(request, 'sitePostavshik/prouductposta.html', context=context)
        else:
                create_anons = Anons(Anons_NameProducts=nameproduct, Anons_SumProduct=sumproduct,
                                     Anons_DateManaProducts = datetime.strptime(dateproduct, '%Y-%m-%d'),
                                     Anons_PriceProduct = priceproduct,
                                     Anons_ExpirationDate = dateExpProduct,
                                     Anons_ID_User = UserID)
                create_anons.save()
                return HttpResponseRedirect("/sitePostavshik/siteorderpostav.html")


class SiteOrderPostavshik(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Поставщик"):
                    idUser = get_user_anons_id(request.session['id_user'])

                    context = {
                         'tablesee': idUser

                    }

                    return render(request, 'sitePostavshik/siteorderpostav.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")

    def post(self, request):
        id = request.POST.get("id")
        if request.POST.get("add"):
            return HttpResponseRedirect('prouductposta.html')
        if id:
            idProduct = get_product_id(id)
            if request.POST.get("delete"):
                delete(id)
                return HttpResponseRedirect('/sitePostavshik/siteorderpostav.html')
            elif request.POST.get("update"):
                context = {
                    'idProduct': idProduct

                }
                return render(request, 'sitePostavshik/PostUpdate.html', context=context)
            elif request.POST.get("update1"):
                id = request.POST.get("id")
                nameProduct = request.POST.get("Name")
                SumProduct = request.POST.get("Sum")
                DateProduct = request.POST.get("DateMan")
                PriceProduct = request.POST.get("Price")
                ExpProduct = request.POST.get("DateExpMan")
                if (ExpProduct <= DateProduct):
                    context = {
                        'idProduct': idProduct,
                        "message": "Срок годности не должен быть меньше чем дата изготовления"
                    }
                    return render(request, 'sitePostavshik/PostUpdate.html', context=context)
                else:
                    update_product(id, nameProduct, SumProduct, DateProduct, PriceProduct, ExpProduct)
                    idUser = get_user_anons_id(request.session['id_user'])
                    context = {
                        'tablesee': idUser
                    }
                    return render(request, 'sitePostavshik/siteorderpostav.html', context=context)
            else:
                idUser = get_user_anons_id(request.session['id_user'])
                context = {
                    'tablesee': idUser
                }
                return render(request, 'sitePostavshik/siteorderpostav.html', context=context)

        else:
            idUser = get_user_anons_id(request.session['id_user'])
            context = {
                'tablesee': idUser
            }

            return render(request, 'sitePostavshik/siteorderpostav.html', context=context)


class SiteAccPostavshik(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Поставщик"):
                    context = {

                    }
                    return render(request, 'sitePostavshik/stieaccpostavshik.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")


class SiteShopProduct(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер магазина"):
                    productsee = getProduct()
                    context = {
                        'productsee': productsee
                    }
                    return render(request, 'siteshop/productshop.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")

    def post(self,request):
        id = request.POST.get("id")
        if request.POST.get("Back"):
            return HttpResponseRedirect('siteordershop.html')
        elif request.POST.get("ADD"):
            return HttpResponseRedirect('orderadd.html')
        else:
            productsee = getProduct()
            context = {
                'productsee': productsee
            }
            return render(request, 'siteshop/productshop.html', context=context)


class SiteShopProductPost(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер магазина"):
                    productsee = getProduct()

                    context = {
                        'products': productsee
                    }
                    return render(request, 'siteshop/orderadd.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")

    def post(self, request ):
        shop_product = request.POST['Products']
        shop_sum = request.POST['Sum']
        shop_name = request.POST['NameShop']
        shop_addres = request.POST['Address']
        UserID = request.session['id_user']
        ProductId = request.POST.get("Products")
        TableProduct = get_products_id(int(shop_product))
        if (int(shop_sum) <= TableProduct.Product_Sum):
            create_order = Order(Order_Name_Product=TableProduct.Product_Name, Order_Sum=shop_sum,
                            Order_Name_Store=shop_name,
                             Order_Address=shop_addres,
                                 Order_Id_User=UserID,
                                 Order_Id_Product=ProductId)
            create_order.save()
            return HttpResponseRedirect('siteordershop.html')
        else:
            messages.error(request,"Нет столько количество продуктов")
        return HttpResponseRedirect('/siteshop/orderadd.html')

class SiteShopSiteOrder(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер магазина"):
                        idUsers = get_user_order_id(request.session['id_user'])
                        context = {
                            'shopsee': idUsers
                        }
                        return render(request, 'siteshop/siteordershop.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")

    def post(self, request):
        id = request.POST.get("id")
        if request.POST.get("addOrder"):
            return HttpResponseRedirect('productshop.html')
        if id:
            idOrders = get_orders_id(id)
            if request.POST.get("deleteOrder"):
                deleteorder(id)
                return HttpResponseRedirect('/siteshop/siteordershop.html')
            elif request.POST.get("updateOrder"):
                productsee = getProduct()
                context = {
                    'products': productsee,
                    'idOrders': idOrders
                }
                return render(request, 'siteshop/UpdateOrder.html', context=context)
        else:
            idUsers = get_user_order_id(request.session['id_user'])
            context = {
                'shopsee': idUsers
            }
            return render(request, 'siteshop/siteordershop.html', context=context)

class SiteAccShop(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер магазина"):
                    context = {
                    }
                    return render(request, 'siteshop/stieaccshop.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")


def logout(request):
    try:
        del request.session['id_user']
        del request.session['priv_user']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


class MainSite(View):
    def get(self, request):
        context = {

        }
        return render(request, 'MainSite/index.html', context=context)


class MainSiteAbout(View):
    def get(self, request):
        context = {

        }
        return render(request, 'MainSite/about.html', context=context)


class MainSiteService(View):
    def get(self, request):
        context = {

        }
        return render(request, 'MainSite/services.html', context=context)


class ErrorSites(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                context = {
                    'Privel': request.session['priv_user']
                }
                return render(request, 'ErrorSite.html', context=context)
        except(KeyError):
            return HttpResponseRedirect("/login.html")

class ErrorSitesProducts(View):
    def get(self, request):
        try:
            if (request.session['id_user']):
                if (request.session['priv_user'] == "Менеджер склада"):
                    context = {
                        'Privel': request.session['priv_user']
                    }
                    return render(request, 'ErrorSiteProducts.html', context=context)
                else:
                    return HttpResponseRedirect("/ErrorSite.html")
        except(KeyError):
            return HttpResponseRedirect("/login.html")

def UpdateOrder(request, id):
        SumProduct = request.POST.get("Sum")
        NameShop = request.POST.get("NameShop")
        AddressShop = request.POST.get("Address")
        IdProduct = request.POST.get("Products")
        TableProduct = get_products_id(int(IdProduct))
        nameProduct = TableProduct.Product_Name
        if (int(SumProduct) <= TableProduct.Product_Sum):
            update_orders(id, nameProduct, SumProduct, NameShop, AddressShop, IdProduct)
            idUsers = get_user_order_id(request.session['id_user'])
            return HttpResponseRedirect('/siteshop/siteordershop.html')
        else:
            messages.error(request,"Нет столько количество продуктов")
        return HttpResponseRedirect('/siteshop/siteordershop.html')
