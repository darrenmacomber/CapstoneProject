# from django.db import models
# from django.contrib.auth.models import User
#
# class UserProfile(models.Model):
#     profile_name = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.Charfield(max_length=100)
#     birthday = models.DateTimeField(null=True, blank=True)
#     location = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
#
#     def __str__(self):
#         return self.profile_name
