from django.contrib import admin
from .models import Profile, UserNote, UserPost, UserFollower, UserFollowing

# Register your models here.

admin.site.register(Profile)
admin.site.register(UserNote)
admin.site.register(UserPost)
admin.site.register(UserFollower)
admin.site.register(UserFollowing)


