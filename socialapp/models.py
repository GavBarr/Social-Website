from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    banner_image = models.ImageField(default='headerpic.jpg', upload_to='header_pictures')
    header_description = models.TextField()
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='test')

    def __str__(self):
        return self.user.username


class UserNote(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    note_header = models.CharField(max_length=100)
    note_details = models.TextField()

    def __str__(self):
        return self.note_header


class UserPost(models.Model):
    #user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    post_header = models.CharField(max_length=100)
    post_details = models.TextField()
    post_likes = models.IntegerField(default='0')
    post_dislikes = models.IntegerField(default='0')

    def __str__(self):
        return self.post_header



class UserFollower(models.Model):
    user = models.CharField(max_length=200)
    follower = models.CharField(max_length=200)

    def __str__(self):
        return self.user

class UserFollowing(models.Model):
    user = models.CharField(max_length=200)
    following = models.CharField(max_length=200)

    def __str__(self):
        return self.user

