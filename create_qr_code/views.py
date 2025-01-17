from django.shortcuts import render

# Create your views here.


def render_create_qr_code_page(request):

    return render(request, "create_qr_code.html")