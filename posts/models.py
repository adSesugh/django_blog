from django.db import models
from django.utils import timezone

class CommonFields(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True



class Post(CommonFields):
    title = models.CharField(max_length=120, null=False)
    content = models.TextField()
    published = models.BooleanField(default=False)
    #published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']
