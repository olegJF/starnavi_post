from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Please enter an email address")
        if not password:
            raise ValueError("Please enter a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            )
        user_obj.set_password(password) 
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email       = models.EmailField(max_length=255, unique=True)
    staff       = models.BooleanField(default=False) 
    admin       = models.BooleanField(default=False)  
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
        
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin