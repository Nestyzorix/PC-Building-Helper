from django.urls import path, include
from .views import configurator_index, configurator_constructor, configurator_help

app_name = "backend_api"
urlpatterns = [
    path("", configurator_index, name="index"),
    path("constructor/", configurator_constructor, name="constructor"),
    path("help/", configurator_help, name="help")
]
