from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("eval/", views.eval_code, name="eval_code"),
    path("pickle/", views.pickle_load, name="pickle_load"),
    path("login/", views.sql_login, name="sql_login"),
    path("ping/", views.shell_exec, name="shell_exec"),
    path("secrets/", views.leak_secrets, name="leak_secrets"),
]
