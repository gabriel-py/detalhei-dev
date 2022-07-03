from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, Group
from .models import UserAccount
from rest_framework import viewsets
from rest_framework.permissions  import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer

# Create your views here.
def go_to_home(request):
    return redirect('http://localhost:3000')



class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)