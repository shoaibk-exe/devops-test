from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("import/", views.dynamic_import, name="dynamic_import"),
    path("welcome/", views.template_injection, name="template_injection"),
    path("xml/", views.xml_parse, name="xml_parse"),
    path("customers/", views.customer_lookup, name="customer_lookup"),
    path("maintenance/", views.maintenance_cmd, name="maintenance_cmd"),
    path("settings/", views.dump_settings, name="dump_settings"),
]
