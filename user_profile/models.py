from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')
    slug = models.SlugField(max_length=200)
                         