from django.shortcuts import render

# Create your views here.

def render_contact_page(request):

    if request.user != "":
        username = request.user
    else:
        username = "none"
    
    return render(request, "contacts.html", context = {"username" : username})