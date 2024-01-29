from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#post_save fires when something is saved to the db

@receiver(post_save, sender=User) #when a user is saved send this signal which can be recieved by this function
def create_profile(sender, instance, created, **kwargs):
    if created: #if the user was created, create a profile object of the user instance
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()

