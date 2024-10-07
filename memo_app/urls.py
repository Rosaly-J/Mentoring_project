"""
URL configuration for memo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from memoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.memo, name='memo'),
    path('memo/new/', views.memo_create, name='memo_create'),
    path('memo/update/<int:memo_id>/', views.memo_update, name='memo_update'),
    path('memo/<int:memo_id>/', views.memo_detail, name='memo_detail'),
    path('memo/delete/<int:memo_id>/', views.memo_delete, name='memo_delete'),

]
