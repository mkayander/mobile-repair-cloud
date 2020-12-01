from django.db import models


class Visitor(models.Model):
    identity = models.CharField(max_length=50)
