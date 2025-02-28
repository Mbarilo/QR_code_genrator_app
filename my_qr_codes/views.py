from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from create_qr_code.models import QrCodes
from registration.models import Profile
import os, datetime


# Create your views here.

def render_my_qr_codes_page(request):
    subscribe = 'standart'
    if request.user.is_authenticated:
        username = request.user
        user = User.objects.get(username = username)
        user_now = Profile.objects.get(user = user)
        user_id = request.user.id
        subscribe = Profile.objects.get(user_id = user_id).subscribe
    else:
        username = "none"
        return redirect("/")

    qr_codes = QrCodes.objects.filter(user_id = username.id)
    len_qr_codes = len(qr_codes)
    finded_qr_codes = []
    qr_codes_pathes = []
    
    if subscribe == "none":
        fmt = "%Y-%m-%d"
        six_months = datetime.timedelta(days=182)
        date = str(datetime.date.today())
        date = datetime.datetime.strptime(date, fmt)
        for code in qr_codes:
            date_qr = str(code.date)
            date_qr = datetime.datetime.strptime(date_qr, fmt)
            if date - date_qr >= six_months:
                code.delete()

    for qr_code in qr_codes:
        qr_codes_pathes.append(qr_code.image)

    if request.method == "POST":
        deleleted_qr_code = request.POST.get("delete")

        find_input = request.POST.get("find_input")


        if "find" in request.POST:
            # qr_codes = []
            for qr_code in qr_codes:
                if find_input in qr_code.name:
                    finded_qr_codes.append(qr_code)



        if deleleted_qr_code != None:
            qr_code_name = QrCodes.objects.get(id = deleleted_qr_code).name
            qr_code_desktop = QrCodes.objects.get(id = deleleted_qr_code).desktop

            if qr_code_desktop:
                os.remove(os.path.abspath(__file__ + f"/../../media/qr_codes/image/{username}/desktop/{qr_code_name}.png"))
                QrCodes.objects.get(id = deleleted_qr_code).delete()
            elif not qr_code_desktop:
                os.remove(os.path.abspath(__file__ + f"/../../media/qr_codes/image/{username}/web/{qr_code_name}.png"))
                QrCodes.objects.get(id = deleleted_qr_code).delete()

            return redirect("/my_qr_codes_page/")

    


    if "find" in request.POST:
        return render(request, "my_qr_codes.html", context = {"username" : username, "qr_codes": finded_qr_codes, "len_qr_codes" : len_qr_codes, "subscribe" : subscribe, "desktop" : user})
    if "find" not in request.POST:
        return render(request, "my_qr_codes.html", context = {"username" : username, "qr_codes": qr_codes, "len_qr_codes" : len_qr_codes, "subscribe" : subscribe, "desktop" : user_now.desktop})
