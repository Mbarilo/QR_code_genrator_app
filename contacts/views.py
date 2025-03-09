from django.shortcuts import render, redirect
from registration.models import Profile 

# Create your views here.

def render_contact_page(request):
    subscribe = 'standart'
    if request.user.is_authenticated:
        username = request.user
        user_id = request.user.id
        user_now = Profile.objects.get(user_id = user_id)
        subscribe = user_now.subscribe
    else:
        username = "none"
        return redirect("/")
    
    return render(request, "contacts.html", context = {"username" : username, "subscribe": subscribe, "user_now" : user_now})