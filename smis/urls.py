from django.urls import path

from . import views
from django.core import serializers

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("Form2/", views.Form2, name="Form2"),
    path("Form3/", views.Form3, name="Form3"),
    path("Form4/", views.Form4, name="Form4"),
    path("get_form1/<int:id>", views.get_form1, name="get_form1"),
    path("get_form2/<int:id>", views.get_form2, name="get_form2"),
    path("get_form4/<int:id>", views.get_form4, name="get_form4"),

]
