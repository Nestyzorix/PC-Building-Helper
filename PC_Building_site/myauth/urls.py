from django.urls import path
from .views import (
    login_view,
    AboutMeView,
    logout_view,
    RegisterView,
)

app_name = "myauth"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),

]