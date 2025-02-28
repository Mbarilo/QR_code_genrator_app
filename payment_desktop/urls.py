from django.urls import path

from .views import render_first_step_payment_desktop_page, render_second_step_payment_desktop_page, render_third_step_payment_desktop_page

urlpatterns = [
    path('first_step_desktop/', render_first_step_payment_desktop_page),
    path('second_step_desktop/', render_second_step_payment_desktop_page),
    path('third_step_desktop/', render_third_step_payment_desktop_page)
]