from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def about(request):
    return render(request, "about.html")


def sessions_view(request):
    return render(request, "sessions.html")


def privacy(request):
    return render(request, 'privacy.html')


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)


def error_403(request, exception=None):
    return render(request, "403.html", status=403)
