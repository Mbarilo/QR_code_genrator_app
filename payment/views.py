from django.shortcuts import render

# Create your views here.

def render_first_step_payment_page(request):
    return render(request, "first_step_payment.html")

def render_second_step_payment_page(request):
    return render(request, "second_step_payment.html")

def render_third_step_payment_page(request):
    return render(request, "third_step_payment.html")