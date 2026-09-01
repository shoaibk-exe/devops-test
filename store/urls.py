from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.unsafe_search, name="unsafe_search"),
    path("diagnostic/", views.run_diagnostic, name="run_diagnostic"),
    path("debug/env/", views.dump_env, name="dump_env"),
]
