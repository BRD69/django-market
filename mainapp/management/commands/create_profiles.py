from django.core.management.base import BaseCommand

from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *agrs, **kwargs):
        for user in ShopUser.objects.filter(shopuserprofile__isnull=True):
            shopuserprofile = ShopUserProfile(user=user)
            shopuserprofile.save()
