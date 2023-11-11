from django.urls import path
from .views import (
    blog,
    blog_page,
)

urlpatterns = [
    path('blog_page/', blog_page, name="blog_page"),
    path('blog/', blog, name="blog"),
]