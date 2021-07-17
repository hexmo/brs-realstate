from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=30)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    district = models.CharField(max_length=15)
    description = models.TextField()
    type = models.CharField(max_length=20)
    price = models.IntegerField()
    created_at = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default='Deleted User')
    posted_on = models.ForeignKey(
        Property, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField()
    comment = models.TextField()
