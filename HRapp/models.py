# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AddDetails(models.Model):
    username = models.CharField(max_length=200)
    emailaddress = models.EmailField(max_length=300)

    def __str__(self):
        return self.username + ' - ' + self.emailaddress