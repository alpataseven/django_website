from django.urls import path
from .views import (
    log_in,
    log_out,
    sign_up,
    home_page
)

urlpatterns = [
    path('', home_page, name="home"),
    path('log_in/', log_in, name="log_in"),
    path('log_out/', log_out, name="log_out"),
    path('sign_up/', sign_up, name="sign_up"),
]