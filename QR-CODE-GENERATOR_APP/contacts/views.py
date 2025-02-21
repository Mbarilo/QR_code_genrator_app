from django.shortcuts import render, redirect
from registration.models import Profile 

# Create your views here.

def render_contact_page(request):
    subscribe = 'standart'
    if request.user.is_authenticated:
        username = request.user
        user_id = request.user.id
        subscribe = Profile.objects.get(user_id = user_id).subscribe
    else:
        username = "none"
        return redirect("/")
    
    return render(request, "contacts.html", context = {"username" : username, "subscribe": subscribe})