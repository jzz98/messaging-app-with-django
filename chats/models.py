from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactsModel(models.Model):
    userd_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_as_user')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_recived')