from django.urls import path

from .views import render_first_step_payment_pro_page, render_second_step_payment_pro_page, render_third_step_payment_pro_page

urlpatterns = [
    path('first_step_pro/', render_first_step_payment_pro_page),
    path('second_step_pro/', render_second_step_payment_pro_page),
    path('third_step_pro/', render_third_step_payment_pro_page)
]