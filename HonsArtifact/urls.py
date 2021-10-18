"""HonsArtifact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^info$',views.InfoPage.as_view(),name='info'),
    url(r'^work$',views.WorkPage.as_view(),name='work'),
    url(r'^contact$',views.ContactPage.as_view(),name='contact'),
    url(r'^SpeedApp/',include('SpeedApp.urls',namespace='SpeedApp')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)