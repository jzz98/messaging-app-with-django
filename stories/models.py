from django.db import models
from django.contrib.auth.models import User
from .utils.user_dirname import user_directory_path

# Create your models here.
class StoriesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    archive_path = models.FileField(upload_to=user_directory_path)
    date_create = models.DateTimeField(auto_now=True)
    date_expire = models.DateTimeField()