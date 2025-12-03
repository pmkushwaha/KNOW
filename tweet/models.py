from django.db import models
from django.contrib.auth.models import User

 
class Tweet (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length="200")
    photo=models.ImageField(upload_to ="photos/",blank=True ,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_pics/', default='default.jpg',blank=True ,null=True)
  
    
    def __str__(self):
        return self.user.username         