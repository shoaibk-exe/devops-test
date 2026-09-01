from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("yaml/", views.unsafe_yaml, name="unsafe_yaml"),
    path("file/", views.path_traversal, name="path_traversal"),
    path("raw-sql/", views.raw_sql, name="raw_sql"),
    path("shell/", views.run_shell, name="run_shell"),
    path("config/", views.expose_config, name="expose_config"),
]
