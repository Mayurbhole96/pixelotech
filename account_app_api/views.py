from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .serializers import *

# cache timeout for OTP
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class SignupView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        mobile_number = request.data.get('mobile_number')
        password = request.data.get('password')
        name = request.data.get('name')
        otp = request.data.get('otp')

        # check if OTP is correct
        cache_key = f'{mobile_number}_otp'
        cached_otp = cache.get(cache_key)

        if not cached_otp or otp != str(cached_otp):
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        # create a new user
        try:
            user = User.objects.create_user(username=mobile_number, password=password,first_name=name)
        except:
            return Response({'error': 'User already exists with this mobile number.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'User created successfully.'}, status=status.HTTP_201_CREATED)

class SigninView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        mobile_number = request.data.get('mobile_number')
        password = request.data.get('password')
        otp = request.data.get('otp')

        # check if OTP is correct
        cache_key = f'{mobile_number}_otp'
        cached_otp = cache.get(cache_key)

        if not cached_otp or otp != str(cached_otp):
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        # authenticate the user
        user = authenticate(request, username=mobile_number, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # login the user
        login(request, user)

        return Response({'success': 'User logged in successfully.'}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('csrftoken')
        response.delete_cookie('sessionid')

        # logout the user
        if request.user.is_authenticated:
            logout(request)

        return response

class SendOtpView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        mobile_number = request.data.get('mobile_number')

        # generate OTP and save to cache
        otp = 123456 # replace with your own OTP generation logic
        cache_key = f'{mobile_number}_otp'
        cache.set(cache_key, otp, timeout=CACHE_TTL)

        # send the OTP to the user via SMS or any other means

        return Response({'success': 'OTP sent successfully.'}, status=status.HTTP_200_OK)

class UserView(APIView):

    def get(self, request):
        user_obj =User.objects.filter(is_active__in = [True]).order_by('-id')
        serializer = UserSerializer(user_obj, many=True)
        if serializer.data:
            return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)