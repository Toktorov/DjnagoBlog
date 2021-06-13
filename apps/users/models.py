from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    nickname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.user.username
        

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_user')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follow_follower')

    def __str__(self):
        return f"{self.sub.id}"