from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    choices = (('F', 'Farmer'), ('N', 'Normal'),('A','Agrovet'),('P','Professional'))
    username = models.CharField(max_length=20,blank=False,null=False)
    email = models.EmailField(unique=True, max_length=255,)
    phone = models.CharField(max_length=13,blank=False,null=False)
    usertype = models.CharField(choices=choices, max_length=2,blank=False,null=False)
    image = models.ImageField(default='',null=True,blank=True)
    date_joined = models.DateTimeField(
        ('date joined'), default=timezone.now
    )

   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username', 'usertype']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True