from django.shortcuts import render, redirect
from .models import RandomCodes
from django.core.mail import send_mail

import random


# Create your views here.

def render_first_step_payment_page(request):


    user_now = request.user

    



    if user_now.is_authenticated:
        if request.method == "POST":

            try:
                random_code_obj = random.randint(99999, 999999)
                RandomCodes.objects.create(random_code = random_code_obj, user = user_now)
            except:
                RandomCodes.objects.get(user_id = user_now.id).delete()
                # RandomCodes.objects.create(random_code = random_code_obj, user = user_now)

            send_mail(
                subject= "Your check code to qr-code generator",
                message= f"Your check code is : {random_code_obj}",
                from_email= "qrcodesgenerator0",
                recipient_list= [f"{user_now.email}"],
                fail_silently= False
            )
            return redirect("/second_step/")
    else:
        return redirect("/registration/")

    
        


    return render(request, "first_step_payment.html")




def render_second_step_payment_page(request):
    
    user_now = request.user

    if request.method == "POST":

        secret_code_model = RandomCodes.objects.get(user_id = user_now.id).random_code
        secret_code_input = request.POST.get("secret_code")

        print(secret_code_input)
        print(secret_code_model)

        if secret_code_input == secret_code_model:
            return redirect("/third_step/")
        else:
            # error = "code not correct"
            return redirect("/")


    return render(request, "second_step_payment.html")

def render_third_step_payment_page(request):
    return render(request, "third_step_payment.html")