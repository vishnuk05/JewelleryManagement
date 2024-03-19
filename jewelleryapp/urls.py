from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/', views.reg_customer, name='reg_customer'),
    path('staff/', views.reg_staff, name='reg_staff'),
    path('contact/', views.contact_info, name='contact'),
    path('cust_login/', views.cust_login , name='cust_login'), 
    path('cust_dashboard/', views.cust_dashboard, name='cust_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('product_delete/<str:pk>', views.product_delete, name='product_delete'),
    path('product_update/<str:pk>', views.product_update, name='product_update'),
    path('staff_logout/', views.staff_logout, name='staff_logout'),
    path('cust_logout/', views.cust_logout, name='cust_logout'),
    path('cust_update/<str:pk>', views.cust_update, name='cust_update'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
    # path('view_cart', views.view_cart, name='view_cart'),


]