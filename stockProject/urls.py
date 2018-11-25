# -*- coding: utf-8 -*-
"""stockProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include,url
import restaurant.views as restaurantView
import stockProject.views as projectView
from django.views.generic.base import RedirectView
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menu/',restaurantView.menu),
    url(r'^meta/',restaurantView.meta),
    url(r'^welcome/',restaurantView.welcome),
    url(r'^restaurants_list/',restaurantView.list_restaurants),
    url(r'^comment/(\d{1,5})/',restaurantView.comment),
    url(r'^set_c/',restaurantView.set_c),
    url(r'^get_c/',restaurantView.get_c),
    url(r'^accounts/login/',projectView.login),
    url(r'^index/',projectView.index),
    url(r'^accounts/logout/',projectView.logout),
    url(r'^accounts/register/$',projectView.register),
    url(r'^$', RedirectView.as_view(url='/app1/'), name='index'),
    url(r'^app1/',  include(('app1.urls', 'app1'), namespace='app1', )),
]
