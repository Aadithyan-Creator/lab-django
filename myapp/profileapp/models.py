from django.db import models
from main.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture =models.ImageField(upload_to=('profiles/'), null=True, blank=True)
    phonenumber = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.user.username
    
    


