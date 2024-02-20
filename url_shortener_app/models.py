from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField(unique=True)
    shortened_url = models.CharField(max_length=100, unique=True)