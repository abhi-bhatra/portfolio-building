from django.db import models

# Create your models here.
class Job(models.Model):
    #save image
    image = models.ImageField(upload_to='images/')
    
    #summary
    summary = models.CharField(max_length=300)
    def __str__(self):
        return self.summary