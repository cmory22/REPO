from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "Kontakty.html", {})

def odtah_view(request, *args, **kwargs):
    return render(request, "odtah.html", {})

def preprava_view(request, *args, **kwargs):
    return render(request, "preprava.html", {})

def autoservis_view(request, *args, **kwargs):
    return render(request, "autoservis.html", {})