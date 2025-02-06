from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, SESSION_KEY
from django.contrib.auth.models import User
from registration.models import Profile


# Create your views here.


def render_login_page(request):
    error = ""

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        name = request.POST.get("name")
        password = str(request.POST.get("password"))

        all_users = Profile.objects.values("user")


        print(name)
        print(password)
        print("")
        print(all_users)
        # print(User.password)
        
        user = authenticate(request, username = name, password = password)





        if user != None:
                login(request, user)
                return redirect("/")
            
        else:
            error = "This user is not exist"

    return render(request, "login.html", context = {"error" : error})
