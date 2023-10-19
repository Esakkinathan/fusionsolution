from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post_image = models.ImageField(null=True,blank=True,upload_to='images/')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content + ' | ' + str(self.date_added)
    
    
    
    
class Comment(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name