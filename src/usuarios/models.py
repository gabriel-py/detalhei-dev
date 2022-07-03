from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.apps import apps

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)

        user = self.model(email=email, username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        username=username
        user = self.model(email=email, username=username, **extra_fields)

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=20, unique=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email

from django.contrib.auth.models import (
    AbstractUser,
    User,
    BaseUserManager,
    PermissionsMixin
)

# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')

#         username = self.normalize_username(username)
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)

#         user.set_password(password)
#         user.save()

#         return user
    
#     def create_superuser(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)

#         user.set_password(password)
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save()

#         return user

# class DetalheiUser(User):
#     email = models.EmailField(max_length=320, unique=True)
#     username = models.CharField(max_length=16, unique=True, null=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager()

#     # USERNAME_FIELD = ['email', 'username']
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'username']


# from django.db.models import Q

# from django.contrib.auth import get_user_model

# MyUser = get_user_model()

# class UsernameOrEmailBackend(object):
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#            # Try to fetch the user by searching the username or email field
#             user = MyUser.objects.get(Q(username=username)|Q(email=username))
#             if user.check_password(password):
#                 return user
#         except MyUser.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             MyUser().set_password(password)