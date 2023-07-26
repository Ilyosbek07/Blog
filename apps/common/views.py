from django.shortcuts import render
from rest_framework import generics

from apps.common.models import User, FAQ, Contact
from apps.common.serializers import UserSerializer, FAQSerializer, ContactSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ContactListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class FAQListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class FAQRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
