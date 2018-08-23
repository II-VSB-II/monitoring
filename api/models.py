from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token as DefaultTokenModel

from .utils import import_callable

from django.db import models
from django.contrib.auth.models import User

# Register your models here.

TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))

class ServerDetail(models.Model):
    user = models.CharField(max_length=20,blank=True)
    ipaddress = models.CharField(max_length=15, unique=True)
    hostname=models.CharField(max_length=100, blank=False)
    fqdn=models.CharField(max_length=100, blank=False)
    sshKey = models.CharField(max_length=1700,blank=False)
    server_user=models.CharField(max_length=20, blank=False)
