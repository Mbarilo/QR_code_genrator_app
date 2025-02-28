"""
URL configuration for qr_code_project project.

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from create_qr_code.views import render_create_qr_code_page
from home.views import render_home
from login.views import render_login_page
from my_qr_codes.views import render_my_qr_codes_page
from registration.views import render_registration
from contacts.views import render_contact_page
from logout_page.views import render_logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_qr_code_page/', render_create_qr_code_page, name = "create_qr_code"),
    path('', render_home, name = "home"),
    path('login_page/', render_login_page, name = "login"),
    path("my_qr_codes_page/", render_my_qr_codes_page, name = "my_qr_codes"),
    path('', include('payment.urls')),
    path('', include('payment_pro.urls')),
    path('registration/', render_registration),
    path('contacts_page/', render_contact_page),
    path('logout_page/', render_logout_page, name = "logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)