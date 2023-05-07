from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Image(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField()

    class Meta:
            db_table = "table_Image"
            verbose_name_plural = "Image"

class UserHistory(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    rating = models.CharField(max_length=50)   #Accept/Reject
    rated_at = models.DateTimeField(default=timezone.localtime)

    class Meta:
        db_table = "table_history"
        verbose_name_plural = "History"
