from django.db import models


class UserInfo(models.Model):
    account = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=12)


