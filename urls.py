from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path("", views.signup, name='signup'),
   path("home", views.index, name='home'),
   path("about", views.home, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("register", views.register, name='register'),
    path("customize", views.customize, name='customize'),
    path("order", views.order, name='order'),
    path('handle-customization/', views.handle_customization, name='handle_customization'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('save_order/', views.save_order, name='save_order'),
    path('order_placed/', views.order_placed, name='order_placed'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('checkout', views.checkout, name='checkout'),
    path('base', views.base, name='base'),   
    path('test', views.test, name='test'),   
    path('login', views.login_user, name='login'),   
    path('signup', views.signup, name='signup'),   
    path('kaam', views.kaam, name='servces'),   
    path('review', views.review, name='review'),   
    path('internship', views.internship, name='internship'),   
    path('terms', views.terms, name='terms'),   
    path('privacy', views.privacy, name='privacy'),   
    
    
       
   
]