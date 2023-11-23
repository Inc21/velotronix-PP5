from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ User Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label="Country", max_length=40,
                           null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
