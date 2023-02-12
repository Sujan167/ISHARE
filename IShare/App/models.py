from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    createdTime = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=False)
    modifyTime = models.DateTimeField(
        auto_now_add=False, auto_now=True, blank=False)

    postData = models.TextField(null=False, blank=False)

    def __str__(self):
        if self.username:
            return str(self.username)
        else:
            return "NAME"


class LikeComment(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=300, blank=False, null=False)
    likeCount = models.IntegerField(null=True, blank=True)
    commentData = models.CharField(max_length=300, blank=False, null=False)
    commentTime = models.DateTimeField(auto_now_add=False, blank=False)

    def __str__(self):
        if self.username:
            return str(self.username)
        else:
            return "NAME"


class UserDetail(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=300, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    # phone = models.InteField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    instaProfile = models.CharField(max_length=300, null=True, blank=True)
    githubProfile = models.CharField(max_length=300, null=True, blank=True)
    linkedinProfile = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        if self.username:
            return str(self.username)
        else:
            return "NAME"
