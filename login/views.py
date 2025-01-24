from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, SESSION_KEY
from django.contrib.auth.models import User

# Create your views here.


def render_login_page(request):
    error = ""

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        name = request.POST.get("name")
        password = str(request.POST.get("password"))
        password_confirm = str(request.POST.get("password_confirm"))

        all_usernames = User.objects.values("username")
        all_passwords = User.objects.values("password")


        print(name)
        print(password)
        print("")
        print(all_usernames)
        print(all_passwords)
        # print(User.password)

        user = authenticate(request, username = name, password = password)



        if password == password_confirm:
            if user != None:
                
                    login(request, user)
                    return redirect("/")
                
            else:
                error = "This user is not exist"
        else:
            error = "Password not match"
        print(error)

    return render(request, "login.html", context = {"error" : error})
