from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("Form2/", views.Form2, name="Form2"),
    path("Form3/", views.Form3, name="Form3"),
    path("Form4/", views.Form4, name="Form4"),

    # path("delete_data/<int:id>", views.delete_data, name="delete_data")

]
