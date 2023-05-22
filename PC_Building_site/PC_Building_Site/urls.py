from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include("backend_api.urls")),
    path('myauth/', include('myauth.urls')),
]
