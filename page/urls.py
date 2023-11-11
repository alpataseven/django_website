from django.urls import path
from .views import (
    home_page,
    log_in,
    sign_up
)

urlpatterns = [
    path('', home_page, name="home"),
    path('log_in/', log_in, name="log_in"),
    path('sign_up/', sign_up, name="sign_up"),
]