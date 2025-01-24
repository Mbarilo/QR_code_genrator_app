from django.urls import path

from .views import render_first_step_payment_page, render_second_step_payment_page, render_third_step_payment_page

urlpatterns = [
    path('first_step/', render_first_step_payment_page),
    path('second_step/', render_second_step_payment_page),
    path('third_step/', render_third_step_payment_page)
]