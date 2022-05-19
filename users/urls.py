from django.urls import path

from users.views import RegisterUserAPIView

urlpatterns = [
    path('users', RegisterUserAPIView.as_view(), name='users-create')
]