from django.shortcuts import render, redirect

# Create your views here.

def render_home(request):

    if request.user.is_authenticated:
        username = request.user
    else:
        username = "none"
    
    return render(request, "home.html", context = {"username" : username})