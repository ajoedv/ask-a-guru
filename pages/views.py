from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def about(request):
    return render(request, "about.html")


def sessions_view(request):
    return render(request, "sessions.html")


def privacy(request):
    return render(request, 'privacy.html')
