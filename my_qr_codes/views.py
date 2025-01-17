from django.shortcuts import render

# Create your views here.

def render_my_qr_codes_page(request):
    
    return render(request, "my_qr_codes.html")