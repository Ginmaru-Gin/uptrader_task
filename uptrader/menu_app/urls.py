from django.urls import path, re_path

from .views import menu_app_view

urlpatterns = [
    re_path(r"^(?!__debug__).*", menu_app_view, name="test_menu"),
]
