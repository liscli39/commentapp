from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    image_id = models.CharField(max_length=255)
    comment = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.image_id + ' - ' + self.author

class Like(models.Model):
    like_id = models.BigAutoField(primary_key=True)
    image_id = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.image_id + ' - ' + self.device_id


class UserCount(models.Model):
    user_count_id = models.BigAutoField(primary_key=True)
    app_id = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
