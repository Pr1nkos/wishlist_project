"""
URL configuration for wishlist_project project.

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
from wishes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.wishlist, name='wishlist'),
    path('delete/<int:wish_id>/', views.delete_wish, name='delete_wish'),
    path('edit/<int:wish_id>/', views.edit_wish, name='edit_wish'),
    path('login/', auth_views.LoginView.as_view(
        template_name='wishes/login.html',
        redirect_authenticated_user=True,
        next_page='/',
        ), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register')
]
"""
Запрос -- URL -- View -- Model -- Template -- Ответ
"""
