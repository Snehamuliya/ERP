from django.contrib import admin
from django.urls import path
from .views import index, signup, product_display, feed, login, logout, profile, supply, ad_profile, ad_sup_profile, buy, my_order
from .views import add_prod, ad_prod_all,up_cus_account, admin_log, a_logout, stock_add, receipt, ad_all_order, ad_all_feed

urlpatterns = [
    path('', index),
    path('sign', signup),
    path('supplier', supply),
    path('home', product_display, name='home'),
    path('feed', feed),
    path('log', login, name='log'),
    path('logout', logout),
    path('ad_logout', a_logout),
    path('admin', admin_log, name='a_log'),
    path("profile", profile,name="c_profile"),
    path("cus_profile", ad_profile),
    path("sup_profile", ad_sup_profile, name='as_data'),
    path("add_product", add_prod),
    path("prod_all", ad_prod_all, name='product'),   
    path("up_c_accout", up_cus_account), 
    path("buy", buy, name="order"),
    path("stock", stock_add, name="stock"),
    path("form", receipt),
    path("m_order", my_order),
    path("ad_order", ad_all_order),
    path("all_feed", ad_all_feed)
]