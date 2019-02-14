from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import random

# Linked to User for extended profile

'''class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mins_left = models.IntegerField(null=True, blank=True, default=100*int(random.random()))
    photo = models.ImageField(upload_to='images', null = True)

# Create and save Profile taking signal from User
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.profile.save()'''

class Game(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images')
    desc = models.CharField(max_length=300, blank=True)
    price = models.FloatField(null=True)
    rating = models.IntegerField(null=True)
    no_of_rating = models.IntegerField(null=True)
    upload_time = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name