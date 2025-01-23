from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.



def render_registration(request):
    error = ""

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        email = request.POST.get("email")

        if password == password_confirm:
            try:
                User.objects.create_user(username = name, password = password, email = email)
                return redirect("/login_page/")
            except:
                error = "this user already registred"
        else:
            error = "passwords not match"

        print(error)


        
        
    return render(request, "registration.html", context= {"error" : error})