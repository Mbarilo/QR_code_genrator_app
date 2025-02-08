from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import QrCodes
from PIL import Image, ImageDraw
from registration.models import Profile
from django.contrib.auth.models import User
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer, SquareModuleDrawer
)
import qrcode
import os


def render_create_qr_code_page(request):



    if request.user.is_authenticated:
        username = request.user
        print(username)
    else:
        username = "none"
        return redirect("/")
    
    user = User.objects.get(username = username)

    user_now = Profile.objects.get(user = user)

    print(user_now.subscribe)

    if request.method == "POST":
        # qr_code_url to encode
        qr_code_url = request.POST.get("url")
        qr_code_name = request.POST.get("name")
        qr_code_color = request.POST.get("color")
        qr_code_back_color = request.POST.get("back_color")

        logotype = request.POST.get("logo")

        dots_form = request.POST.get("dots")
        eye_form = request.POST.get("eye")

        frame_around =  request.POST.get("circle")

        print("\n\n\n\n\n",frame_around, "\n\n\n\n\n\n\n")

        if qr_code_name == "":
            return redirect("/create_qr_code_page/")
               

        qr_code = qrcode.QRCode()
        qr_code.add_data(qr_code_url)
        qr_code.make()


        eye_drawer_module = SquareModuleDrawer()
        dots_drawer_module = SquareModuleDrawer()


        if eye_form == "circle" or eye_form == "Circle":
            eye_drawer_module = CircleModuleDrawer()
        elif dots_form == "circle" or dots_form == "Circle":
            dots_drawer_module = CircleModuleDrawer(resample_method=None)



        img = qr_code.make_image(fill_color = qr_code_color, back_color = qr_code_back_color, module_drawer= dots_drawer_module, eye_drawer=eye_drawer_module, image_factory=StyledPilImage)



        if frame_around == "on":
            draw = ImageDraw.Draw(img)

            draw.ellipse(
                (0, 0, img.size[1], img.size[1]),
                fill = None,
                outline ='black',
                width=5
            )


        qr_codes = QrCodes.objects.filter(user_id = username.id)

        qrcode_names = []

        for qr_code in qr_codes:
            qrcode_names.append(qr_code.name)

        print(len(qr_codes) + 1)

        maximum_qr_codes = 0

        if user_now.subscribe == "none":
            maximum_qr_codes = 1
        elif user_now.subscribe == "standart":
            maximum_qr_codes = 10
        elif user_now.subscribe == "pro":
            maximum_qr_codes = 100

        if qr_code_name not in qrcode_names:

            if len(qr_codes) < maximum_qr_codes:

                if "save" in request.POST:
                    # try:
                    img.save(os.path.abspath(__file__ + f"/../../media/qr_codes/demo/{username}_qrcode.png"))
                    QrCodes.objects.create(name = qr_code_name, image = f"/../../media/qr_codes/image/{username}/{qr_code_name}.png", user = username)
                    img.save(os.path.abspath(__file__ + f"/../../media/qr_codes/image/{username}/{qr_code_name}.png"))
                    # except:
                    #     error = "this name already used"
        return redirect("/create_qr_code_page/")


    return render(request, "create_qr_code.html", context = {"username" : username, })

