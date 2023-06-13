from django.shortcuts import render

# Create your views here.

def testfarma(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "aboutUs.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def terms(request):
    return render(request, "termsandconditions.html")

