from django.db import models
from django.contrib.auth.models import User

import datetime

'''Represents the additional data associated with the User'''
# Extra data that is used to populate the Profile page and MyShelf.
# Spoiler Protection is a boolean parameter that prevents user from reading comment text further in a given Book than they are.
# Date is an extracted string made from a datetime object.
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    spoiler_protection = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def prettybirthday(self):
        converted = self.birthday.strftime('%B %d, %Y')
        return converted
