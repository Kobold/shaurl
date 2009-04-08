from django.db import models

class UrlMapping(models.Model):
    """maps from a SHA hash to a URL"""
    
    url = models.URLField()
    sha_hash = models.CharField(max_length=40)
