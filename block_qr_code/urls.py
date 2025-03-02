from django.urls import path
from django.http import HttpResponse
from .views import render_block_page

urlpatterns = [
    path('block_qr_code/', render_block_page)
]

