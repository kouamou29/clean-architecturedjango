from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    # You can add additional fields here if needed
    # For example:
    # bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, related_name='user',  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title