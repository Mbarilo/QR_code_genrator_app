from django.shortcuts import render

# Create your views here.


def render_create_qr_code_page(request):

    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"

    return render(request, "create_qr_code.html", context = {"username" : username})