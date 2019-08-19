"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views

from django.urls import path, re_path, include
from main_page import views
from blog import views as blogViews

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('data_viz/',include('data_viz.urls')),
    path('main_page/',include('main_page.urls')),
    path('education/',include('education.urls')),
    path('about_me/',include('about_me.urls')),
    path('psql_db/',include('psql_db.urls')),

    path('blog/',include('blog.urls')),


    #re_path('accounts/login/$',blogViews.login,name='login'),
    #re_path('accounts/logout/$',blogViews.logout,name='logout',kwargs={'next_page':'/'}),



]
