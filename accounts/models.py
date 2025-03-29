from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_mentor = models.BooleanField(default=False)  # True if the user is a mentor
    is_mentee = models.BooleanField(default=True)  # True if the user is a mentee
    skills = models.ManyToManyField('Skill', blank=True, related_name="users")

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Skill(models.Model):
    name = models.CharField(max_length=100)
