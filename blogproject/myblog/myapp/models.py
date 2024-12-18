from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField (max_length=200)
    description = models.TextField()
    posted_by = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=datetime.now)
    def __blg__(self):
        return self.title
    
    


