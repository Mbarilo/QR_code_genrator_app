from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from create_qr_code.models import QrCodes
import os


# Create your views here.

def render_my_qr_codes_page(request):
    
    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"
        return redirect("/")

    qr_codes = QrCodes.objects.filter(user_id = username.id)
    qr_codes_pathes = []

    for qr_code in qr_codes:
        qr_codes_pathes.append(qr_code.image)

    if request.method == "POST":
        deleleted_qr_code = request.POST.get("delete")

        qr_code_name = QrCodes.objects.get(id = deleleted_qr_code).name

        if deleleted_qr_code != None:

            QrCodes.objects.get(id = deleleted_qr_code).delete()
            os.remove(os.path.abspath(__file__ + f"/../../media/qr_codes/image/{username}_{qr_code_name}.png"))

            return redirect("/my_qr_codes_page/")



    return render(request, "my_qr_codes.html", context = {"username" : username, "qr_codes": qr_codes})