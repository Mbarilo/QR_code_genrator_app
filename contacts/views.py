from django.shortcuts import render

# Create your views here.

def render_contact_page(request):
    return render(request, "contacts.html")