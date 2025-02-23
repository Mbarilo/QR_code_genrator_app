from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from registration.models import Profile
from django.contrib.auth.hashers import make_password
import os
from PIL import Image
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

        print(name)
        print(password)

        # User.objects.create_user(username = name, password = password, email = email)
        # print(user)
        print(Profile.user)

        print(User(username = name, password = password))
        

        # User.objects.create(username = name, password = password)



        if password == password_confirm:
            try:
                user = User(username = name, password = make_password(password))
                user.save()
                username = user.username
                no_image = Image.open(os.path.abspath(__file__ + f"/../../media/no_image.png"))
                no_image.save(os.path.abspath(__file__ + f"/../../media/qr_codes/demo/{username}_qrcode.png"))
                Profile.objects.create(user = user, subscribe = "none")
                os.makedirs(os.path.abspath(__file__ + f"/../../media/qr_codes/image/{name}"))
                return redirect("/login_page/")
            except:
                error = "this user already registred"
        else:
            error = "passwords not match"

        print(error)


        
        
    return render(request, "registration.html", context= {"error" : error})