from django.db import models

# account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(AbstractUser):
    ROLE_CHOICES = (
        ("buyer", "Buyer"),
        ("vendor", "Vendor"),
        ("delivery", "Delivery"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    def __str__(self):
        return f"{self.username} - {self.role}"


class BuyerProfile(models.Model):
    user = models.OneToOneField(UserRole, on_delete=models.CASCADE, related_name="buyer_profile")
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.user.username} - {self.user.role}"


class VendorProfile(models.Model):
    user = models.OneToOneField(UserRole, on_delete=models.CASCADE, related_name="vendor_profile")
    business_name = models.CharField(max_length=255)
    business_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.user.username} - {self.user.role}"


class DeliveryProfile(models.Model):
    user = models.OneToOneField(UserRole, on_delete=models.CASCADE, related_name="delivery_profile")
    vehicle_type = models.CharField(max_length=50)
    nin = models.CharField(max_length=11)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=6)
    next_of_kin = models.CharField(max_length=20)
    guarantor1 = models.CharField(max_length=100)
    guarantor2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.user.role}"


# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

