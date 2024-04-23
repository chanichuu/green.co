from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = (
        User.objects.all()
    )  # get all of the users to make sure we don't create the same again
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # allow anyone to access this view


class UserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)
