from django.shortcuts import render, redirect

# Create your views here.


def render_create_qr_code_page(request):

    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"
        return redirect("/")

    return render(request, "create_qr_code.html", context = {"username" : username})