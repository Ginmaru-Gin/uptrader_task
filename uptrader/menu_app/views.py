from django.shortcuts import render


def menu_app_view(request):
    return render(request, "menu_app.html")
