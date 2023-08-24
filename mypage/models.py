from django.db import models

class LifeQuotes(models.Model):
    sentence = models.CharField(max_length=300)