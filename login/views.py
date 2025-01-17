from django.shortcuts import render, redirect
from registration.models import Users
from django.contrib.auth import login, authenticate


# Create your views here.

def render_login_page(request):

    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")

        all_usernames = Users.objects.values("name")
        all_passwords = Users.objects.values("password")
        all_emails = Users.objects.values("email")

        usernames = []
        passwords = []
        emails = []
        


        for name_index in all_usernames:
            usernames.append(name_index["name"])

        for password_index in all_passwords:
            passwords.append(password_index["password"])

        for email_index in all_emails:
            emails.append(email_index["email"])

        if name in usernames and int(password) in passwords and email in emails:
            user = authenticate(request, name = name, password = password, email = email)
            if user:
                login(request, user)
            else:
                print("user is not exist")
            return redirect("/home/")

        print(usernames)
        print(passwords)
        print(emails)

        print(name)
        print(password)
        print(email)

    return render(request, "login.html")