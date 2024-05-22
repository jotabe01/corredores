from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [
    path('', index , name="index"),
    path('inicio_s', inicio_s , name="inicio_s"),
    path('sesion/', login_view, name="sesion"),
    path('dashboard', dashboard, name="dashboard"),
    path('logout_view', logout_view, name="logout_view"),
    path('propiedades', propiedades, name="propiedades"),
    path('popietarios', propietarios, name="propietarios"),
    path('arrendatarios',arrendatarios, name="arrendatarios"),
    path('finanzas',finanzas, name="finanzas"),
    path('contratos',contratos, name="contratos"),
    path('wallet', wallet, name="wallet"),
    path('registro', registro , name="registro"),
    path('tables', tables, name="tables"),
    path('registrar', registrar, name="registrar"),
    path('view_arrend', view_arrend, name="view_arrend"),
    path('addpropiedad',addpropiedad, name="addpropiedad"),
    path('addcontrato', addcontrato, name="addcontrato"),
    path('addpropietario', addpropietario, name="addpropietario"),
    path('addarrendatario', addarrendatario, name="addarrendatario"),
    path('detallepropiedad', detallepropiedad, name="detallepropiedad"),
    path('detallearrendatario', detallearrendatario, name="detallearrendatario"),
    path('detallepropietario', detallepropietario, name="detallepropietario"),
    path('pagar', pagar, name="pagar"),
    path('perfilu', perfilu, name="perfilu"),
    path('contactanos',contactanos, name="contactanos"),
    
    
]
