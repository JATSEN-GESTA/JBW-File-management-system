from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerLog, name='customerlogin'),
    path('customerlogin/', views.CustomerLog, name='customerlogin'),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('mainwindow/', views.main_window, name='mainwindow'),
    path('email/', views.email, name='email'),
    path('request/', views.requestq, name='request'),
    path('respond/', views.respondq, name='respond'),
    path('delivery/', views.delivery, name='delivery'),
    path('tools/', views.tools, name='tools'),
    path('quotation/', views.retrieve, name='retrieve'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('update/<str:pk>/', views.UpdateQuotation, name='update'), 
    path('homecustomer/', views.CustomerHome, name='customerhome'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('PDF/<str:pk>/', views.requestpdf, name='requestpdf'),
]