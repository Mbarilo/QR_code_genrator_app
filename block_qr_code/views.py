from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from registration.models import Profile
from create_qr_code.models import QrCodes
from time import gmtime, strftime


# Create your views here.


def render_block_page(request, qr_id):

    username = request.user

    user = User.objects.get(username = username)

    user_now = Profile.objects.get(user = user)



    qr_code = QrCodes.objects.get(user_id = user_now.user.id, name = qr_id)

    qr_code_url = qr_code.url

    print(qr_code.date)

    qr_code_date = int(str(qr_code.date).split("-")[1])

    month_now = int(strftime("%m"))

    print(qr_code_date, "\n", month_now)

    if month_now - qr_code_date >= 6:
        qr_code_url = "this qr_code overdue"
        return render(request, "redirect.html", context= {"data_qr_code" : qr_code_url})

    if qr_code.desktop:
        return render(request, "redirect.html", context= {"data_qr_code" : qr_code_url})
    else:
        return redirect(qr_code_url)