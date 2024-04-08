from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_images')
    dob=models.DateField()
    phone=models.CharField(max_length=100)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    followed_by= models.ManyToManyField(User,related_name='follower')

class Posts(models.Model):
    title=models.CharField(max_length=100)
    body =models.CharField(max_length=300)
    image=models.ImageField(upload_to='post_images',null=True,blank=True)
    datetime=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    liked_by=models.ManyToManyField(User,related_name='user')
    def __str__(self) -> str:
        return self.title
    def fetch_comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)

