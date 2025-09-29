from django.contrib import admin
from user_app.models import UserRole, BuyerProfile, VendorProfile, DeliveryProfile

# Register your models here.
admin.site.register(UserRole)
admin.site.register(BuyerProfile)
admin.site.register(VendorProfile)
admin.site.register(DeliveryProfile)

