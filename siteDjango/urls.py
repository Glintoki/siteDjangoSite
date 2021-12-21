from appDjango.views import *
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainSite.as_view()),
    path('MainSite/index.html', MainSite.as_view()),
    path('MainSite/about.html', MainSiteAbout.as_view()),
    path('MainSite/services.html', MainSiteService.as_view()),
    path('login.html', Login.as_view()),
    path('registration.html', Registration.as_view()),
    path('siteannons.html', SiteAnons.as_view()),
    path('siteorder.html', SiteOrder.as_view()),
    path('stieacc.html', SiteAcc.as_view()),
    path('productssite.html', ProductSite.as_view()),
    path('sitePostavshik/siteorderpostav.html', SiteOrderPostavshik.as_view()),
    path('sitePostavshik/stieaccpostavshik.html', SiteAccPostavshik.as_view()),
    path('sitePostavshik/prouductposta.html', PostavshikProduct.as_view()),
    path('siteshop/productshop.html', SiteShopProduct.as_view()),
    path('siteshop/orderadd.html', SiteShopProductPost.as_view()),
    path('siteshop/siteordershop.html', SiteShopSiteOrder.as_view()),
    path('siteshop/stieaccshop.html', SiteAccShop.as_view()),
    path('ErrorSite.html', ErrorSites.as_view()),
    path('siteshop/<int:id>/UpdateOrder.html', UpdateOrder),
    path('ErrorSiteProducts.html', ErrorSitesProducts.as_view()),
    path('logout/', logout, name='logout')
]
