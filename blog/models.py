from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):# this is a dunder str method why we have used it is when we were using the post.object.all() to filter the database we were not getting a decriptive information instead just some ids with this we are returning the title and hence will get that
        return self.title








