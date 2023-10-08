from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.content
        
class PrivateMessage(Message):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_name')