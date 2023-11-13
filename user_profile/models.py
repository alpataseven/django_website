from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField kullanma sebebim sadece bir kullanıcı hesabu kurulabilecek olmasıdır.
    avatar = models.ImageField(upload_to = 'avatar') 

