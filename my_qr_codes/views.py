from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def render_my_qr_codes_page(request):
    
    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"
        return redirect("/")

    return render(request, "my_qr_codes.html", context = {"username" : username})