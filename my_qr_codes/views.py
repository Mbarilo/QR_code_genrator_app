from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def render_my_qr_codes_page(request):
    
    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"

    return render(request, "my_qr_codes.html", context = {"username" : username})