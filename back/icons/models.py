from django.db import models


class bot(models.Model):
    icon = models.ImageField(upload_to="bots", null=True)

class shroom(models.Model):
    icon = models.ImageField(upload_to="shrooms", null=True)