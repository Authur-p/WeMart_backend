# account/serializers.py
from rest_framework import serializers
from user_app.models import UserRole, BuyerProfile, VendorProfile, DeliveryProfile
from django.contrib.auth.hashers import make_password

class BuyerRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = UserRole
        fields = ["username", "email", "password", "password2", "first_name", "last_name", "phone"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords must match'})

        if UserRole.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already registered'})

        user = UserRole(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            role='buyer'
        )
        user.set_password(password)
        user.save()

        BuyerProfile.objects.create(user=user, phone=self.validated_data['phone'])

        return user


class VendorRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    business_name = serializers.CharField(write_only=True)
    business_address = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = UserRole
        fields = ["username", "email", "password", "password2", "business_name",
                  "business_address", "phone", "first_name", "last_name"]

    def save(self, **kwargs):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords must match"})

        if UserRole.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({"error": "Email already registered"})

        user = UserRole(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            role="vendor",
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.set_password(password)
        user.save()

        VendorProfile.objects.create(
            user=user,
            business_name=self.validated_data["business_name"],
            business_address=self.validated_data["business_address"],
            phone=self.validated_data["phone"],
        )

        return user


class DeliveryRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    vehicle_type = serializers.CharField(write_only=True)
    nin = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    next_of_kin = serializers.CharField(write_only=True)
    guarantor1 = serializers.CharField(write_only=True)
    guarantor2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserRole
        fields = ["username", "email", "password", "password2", "vehicle_type", "nin",
                  "gender", "next_of_kin", "guarantor1", "guarantor2", "phone", "first_name", "last_name"]

    def save(self, **kwargs):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords must match"})

        if UserRole.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({"error": "Email already registered"})

        user = UserRole(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            role="delivery",
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.set_password(password)
        user.save()

        DeliveryProfile.objects.create(
            user=user,
            phone=self.validated_data["phone"],
            # nin=self.validated_data["nin"],
            nin = make_password(self.validated_data["nin"]),
            gender=self.validated_data["gender"],
            next_of_kin=self.validated_data["next_of_kin"],
            guarantor1=self.validated_data["guarantor1"],
            guarantor2=self.validated_data["guarantor2"],
            vehicle_type=self.validated_data["vehicle_type"],


        )

        return user
