from django.db import models

class User(models.Model):
    user_id     = models.AutoField(primary_key=True)
    email       = models.CharField(blank=False, max_length=120, unique=True)
    counter     = models.IntegerField(default=0)
    is_active   = models.BooleanField(default=False)
    token       = models.CharField(max_length=16)
