"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from app import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter() 
router.register(r'users', views.UserViewSet)
router.register(r'trans', views.TransactionViewSet)
router.register(r'firm', views.FirmViewSet)
router.register(r'product', views.ProductViewSet)

router.register(r'firm/<int:user_id>', views.FirmViewSet)
router.register(r'users/<int:user_id>', views.UserViewSet)
router.register(r'product/<int:user_id>', views.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += router.urls