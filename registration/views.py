from django.shortcuts import render, redirect
from .models import Users
# Create your views here.

def render_registration(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = Users(name = name, password = password, email = email)

        try:
            user.save()
            return redirect("/registration/")
        except:
            return redirect("/registration/")
    return render(request, "registration.html")