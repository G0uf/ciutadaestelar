from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from naus.models import Nau

class Hangar(models.Model):
    usuari = models.ForeignKey(User)
    credits = models.IntegerField( default=30, help_text="Punts")
    naus = models.ManyToManyField(Nau, verbose_name="Naus", help_text="Les naus que conte el hangar")
