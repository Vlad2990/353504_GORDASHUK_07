from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('', main, name="main"),
    path('register/', register, name='register'),
    path('feedback/', create_feedback, name='feedback'),
    path('reviews/', show_reviews, name='reviews'),
    path('about/', show_about, name='about'),
    path('news/', show_news, name='news'),
    path('qa/', show_qa, name='qa'),
    path('policies/', show_policies, name='policies'),
    path('promocodes/', show_promocodes, name='promocodes'),
    path('contacts/', show_contacts, name='contacts'),
    path('cart/', view_cart, name='cart'),
    re_path(r'^add-to-cart/(?P<product_id>\d+)/$', add_to_cart, name='add_to_cart'),
    re_path(r'^cart/remove/(?P<item_id>\d+)/$', remove_from_cart, name='remove_from_cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('pickup/', view_pickup, name='pickups'),
    path('admin/addproduct/', add_product, name='addproduct'),
    path('admin/addprovider/', add_provider, name='addprovider'),
    path('admin/viewproducts', show_products, name='viewproducts'),
    path('admin/deleteprod/<int:prod_id>/', delete_product, name='delete_product'),
    path('admin/editprod/<int:prod_id>/', edit_product, name='edit_product'),
    path('admin/vieworders/', show_orders, name='vieworders'),
    path('admin/viewproviders/', show_providers, name='viewproviders'),  
    path('admin/deleteprovider/<int:pr_id>/', delete_provider, name='delete_provider'),
    path('admin/editprovider/<int:pr_id>/', edit_provider, name='edit_provider'), 
    path('admin/stats/', show_stats, name='showstats'), 
]