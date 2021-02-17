from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


def delta_expires_datetime():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="возраст", default=18)
    avatar = models.ImageField(verbose_name="аватар", upload_to="users_avatar_images", blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires: datetime = models.DateTimeField(default=delta_expires_datetime)

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = "W"

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    user = models.OneToOneField(ShopUser, on_delete=models.CASCADE)
    aboutMe = models.CharField(verbose_name='о себе', max_length=128, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            print("create ShopUserProfile")
            ShopUserProfile.objects.create(user=instance)
        else:
            print("save ShopUserProfile")
            instance.shopuserprofile.save()
