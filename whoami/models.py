from django.db import models

# Database table for the course entries
class Post(models.Model):
    download_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=255)
