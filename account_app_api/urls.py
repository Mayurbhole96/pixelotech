from django.urls import path
from .views import SignupView, SigninView, SendOtpView, LogoutView, UserView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('sendotp/', SendOtpView.as_view(), name='sendotp'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view()),
]
