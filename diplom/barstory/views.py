from django.shortcuts import render


def home_page(request):
    return render(request, 'barstory/index.html')
