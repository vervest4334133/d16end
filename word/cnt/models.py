from django.db import models

class Word(models.Model):
    file = models.FileField()

