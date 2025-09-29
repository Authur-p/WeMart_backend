from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import BuyerRegistrationSerializer, VendorRegistrationSerializer, DeliveryRegistrationSerializer


@api_view(['POST'])
def logout(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def buyerRegistration(request):

    if request.method == 'POST':
        serializer = BuyerRegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = ("Registration Successful!!", status.HTTP_201_CREATED)
            data['user'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            data = serializer.errors

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


@api_view(['POST'])
def vendorRegistration(request):

    if request.method == 'POST':
        serializer = VendorRegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = ("Registration Successful!!", status.HTTP_201_CREATED)
            data['user'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }


        else:
            data = serializer.errors

        return Response(data)


@api_view(['POST'])
def deliveryRegistration(request):

    if request.method == 'POST':
        serializer = DeliveryRegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = ("Registration Successful!!", status.HTTP_201_CREATED)
            data['user'] = account.username
            data['email'] = account.email

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }


        else:
            data = serializer.errors

        return Response(data)