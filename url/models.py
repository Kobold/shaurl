from django.db import models

class UrlMapping(models.Model):
    """maps from a SHA hash to a URL"""
    
    url = models.URLField(unique=True)
    sha_hash = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return '/%s' % self.sha_hash

    class Meta:
        ordering = ['-created']
