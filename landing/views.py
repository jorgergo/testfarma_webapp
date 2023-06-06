from django.shortcuts import render

# Create your views here.

def testfarma(request):
    return render(request, "testfarma.html")

def services(request):
    return render(request, "services.html")

def termsandconditions(request):
    return render(request, "termsandconditions.html")