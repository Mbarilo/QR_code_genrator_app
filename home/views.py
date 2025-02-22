from django.shortcuts import render, redirect
from registration.models import Profile

# Create your views here.

def render_home(request):
    subscribe = 'standart'
    if request.user.is_authenticated:
        username = request.user
        user_id = request.user.id
        subscribe = Profile.objects.get(user_id = user_id).subscribe
    else:
        username = "none"
    
    return render(request, "home.html", context = {"username" : username, "subscribe": subscribe})