from django.shortcuts import render, redirect
from registration.models import Profile

# Create your views here.

def render_home(request):
    subscribe = 'standart'
    user_now = "none"
    if request.user.is_authenticated:
        username = request.user
        user_id = request.user.id
        user_now = Profile.objects.get(user_id = user_id)
        subscribe = user_now.subscribe
    else:
        username = "none"
    
    return render(request, "home.html", context = {"username" : username, "subscribe": subscribe, "user_now" : user_now})