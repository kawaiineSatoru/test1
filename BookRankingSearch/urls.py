"""BookRankingSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# 這三行 import 在各個 application 中定義的網頁資料
from main_page import views  as m #main_page_view
from search_result import views  as s # search_result_view
from user_profile import views  as u# user_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', m.main_page_view),
    path('result/', s.search_result_view),
    path('user/', u.user_profile_view),
]

