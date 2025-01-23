from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.


def render_logout_page(request):


    logout(request)
    return redirect("/")