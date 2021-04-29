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
    path("registration/<int:id>", views.update_farmer, name="registration"),
    path("report_reg_all/", views.report_reg_all, name="report_reg_all"),
    path("report_indvidual/", views.report_indvidual, name="report_indvidual"),
    path("report_mull_all/", views.report_mull_all, name="report_mull_all"),
    path("report_prod_all/", views.report_prod_all, name="report_prod_all"),
    path("report_sub_all/", views.report_sub_all, name="report_sub_all"),
    path("update_farmer/<int:id>", views.update_farmer, name="update_farmer"),
    path("delete_farmer/<int:id>", views.delete_farmer, name="delete_farmer"),



]
