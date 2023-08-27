from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('user/',views.user, name='user'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('products/<int:product_id>/',views.products, name='products'),
    path('product_list/',views.product_list, name='product_list'),
]