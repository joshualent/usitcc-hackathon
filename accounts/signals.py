from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser  # First import the CustomUser model
from .models import Profile     # Then import the Profile model

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a profile when a CustomUser is created."""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """Automatically save the profile when the CustomUser is saved."""
    instance.profile.save()
