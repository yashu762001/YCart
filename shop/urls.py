"""YShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

#  . implies to import a file from the current package.

urlpatterns = [

    path("", views.home, name = "Home"),
    path("latest", views.index, name="Latest Products"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Track Your Product"),
    # path("search/",views.search,name="Search Products"),
    path("product/<int:id>", views.product, name="View Your Product"),
    path("checkout/", views.checkout, name="CheckOut"),
    path('handlerequest/', views.handlerequest, name="handlerequest")

]
