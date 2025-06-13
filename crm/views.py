from rest_framework import viewsets , generics
from .models import Customer, Contact
from .serializers import CustomerSerializer, ContactSerializer , RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer