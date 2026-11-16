"""
URL configuration for business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

urlpatterns = [
    path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('services/', views.services, name='services'),
path('portfolio/', views.portfolio, name='portfolio'),
path('portfolio/details/', views.portfolio_details, name='portfolio_details'),
path('team/', views.team, name='team'),
path('pricing/', views.pricing, name='pricing'),
path('blog/', views.blog, name='blog'),
path('blog/details/', views.blog_details, name='blog_details'),
path('contact/', views.contact, name='contact'),
path('dashboard/login/', views.dashboard_login, name='dashboard_login'),
path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),
path('dashboard/', views.dashboard_home, name='dashboard_home'),
]
