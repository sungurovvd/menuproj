"""MenuProject URL Configuration

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
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', TemplateView.as_view(template_name='page.html')),
    path('first/1/', TemplateView.as_view(template_name='page.html'), name = 'first1'),
    path('first/2/', TemplateView.as_view(template_name='page.html')),
    path('second/', TemplateView.as_view(template_name='page.html')),
    path('first/1/1/', TemplateView.as_view(template_name='page.html')),
    path('first/1/2/', TemplateView.as_view(template_name='page.html')),
    path('first/1/3/', TemplateView.as_view(template_name='page.html')),
    path('first/1/4/', TemplateView.as_view(template_name='page.html')),
    path('first/1/1/1/', TemplateView.as_view(template_name='page.html')),
    path('first/1/1/2/', TemplateView.as_view(template_name='page.html')),
]
